import pandas as pd
import os
import numpy as np
import sys

DATA_SOURCES = {"courses": "course2015_2017_ALL.csv",
				"students": "students2015_2017_ALL.csv",
				"demographics": "demographics2015_2017_ALL.csv"}
				
COLMAPS = {
    'courses': {
        'sid': ['id'],
        'cid': ['DISC', 'CNUM', 'HRS'],
        'iid': ['INSTR_LNAME', 'INSTR_FNAME'],
        'termnum': ['TERMBNR'],
        'iclass': ['class'],
        'irank': ['instr_rank'],
        'itenure': ['instr_tenure'],
        'cdisc': ['DISC'],
    },
    'demographics': {
        'srace': ['race'],
        'sex': ['SEX']
    },
    'students': {
        'major': ['PMAJR'],
		'cohort': ['cohort']
    }
}

DUMMYVAR = {'major'}

class dataset(object):

	def __init__(self, input_path):
		self.register(input_path)
	
	def add_table(self, table, tablename):
		setattr(self, tablename, table)

	def register(self, input_path):
		# register data from data sources
		for src_name, fname in DATA_SOURCES.items():
			table = pd.read_csv(os.path.join(input_path, fname))
			self.add_table(table, src_name)
					
	def map_col(self, how):
		
		courses_cols = ['id', 'TERMBNR', 'DISC', 'CNUM', 'GRADE', 'HRS',
                        'grdpts', 'INSTR_LNAME', 'INSTR_FNAME', 'class',
						'instr_rank', 'instr_tenure']
		courses = self.courses[courses_cols]
		
		# add students data
		students = self.students
		data = pd.merge(courses, students, 
						on=['id', 'TERMBNR'], 
						how='inner')
						
		# remove NAN grades
		data = data[~np.isnan(data.grdpts)] 
								
		# add demographics data
		demographics = self.demographics
		if(how == 'smaller') | (how is None):
			data = pd.merge(data, demographics, on='id', how='inner')
		elif how == 'all':
			data = pd.merge(data, demographics, on='id', how='left')
			
		# add unknown tags for nan demo data
		data['race'] = data['race'].fillna('UNKNOWN')
		data['SEX'] = data['SEX'].fillna('N')
			
		
		# transform in numerical values categorical data	
		data['iid'] = data[COLMAPS['courses']['iid']].sum(axis=1).astype('category').cat.codes
		data['cid'] = data[COLMAPS['courses']['cid']].astype(str).sum(axis=1).astype('category').cat.codes
		data['sid'] = data['id'].astype('category').cat.codes
		
		features_list = []
		for src_name, coldic in COLMAPS.items():
			for colname, collist in coldic.items():
				if (colname != 'cid') & (colname != 'iid'):
					data[colname] = data[collist[0]].astype('category').cat.codes
					code_min = data[colname].min()
					data[colname] = data[colname] - code_min
				features_list.append(colname)
				
		# add a flag for stem major
		stem_list =['CS', 'INFT', 'FRSC', 'BIOL', 'CHEM', 
               'CPE', 'BIOE', 'PSYC', 'NEUR', 'ASTR', 'ESC',
               'CEIE', 'ACCT', 'ME', 'EVSS', 'PHYS', 'GAME',
               'AOES', 'ACS', 'MLAB', 'CYSE', 'MATH', 'ELEN', 'ISOM']
		data['in_stem'] = (data.COHORT_PMAJR.isin(stem_list)).astype('int32')
				
		# add grade evaluation
		gradevals = ['grdpts']
		
		# add dummy for failing
		data['failing'] = (data.grdpts == 0).astype('int32')
		first_time = data[data.failing == 1].groupby('sid')[['termnum']].min()
		first_time.columns = ['first_time']
		data = pd.merge(data, first_time, left_on='sid', right_index=True, how='outer')
		data['first_time'] = data['first_time'].fillna(15)
		data['has_failed'] = (data.termnum > data.first_time).astype('int32')
		
		
		# add dummy for minority group
		data['is_black'] = (data.race == "BLACK").astype('int32')
		data['is_male'] = (data.SEX == "M").astype('int32')
		
		# compute average grade until termnum
		termmax = data.termnum.max()
		termmin = data.termnum.min()
		for t in np.arange(termmin + 1, termmax + 1):

			d = data[data.termnum < t].groupby('sid')[['grdpts']].mean()
			d.columns = ['grade_previous']
			d['termnum'] = t
			data = pd.merge(data, d.reset_index(), on=['sid', 'termnum'], how='left')
			data.loc[data.termnum == t, 'cum_grade_previous'] = data['grade_previous']
			data.drop('grade_previous', axis=1, inplace=True)
			
		# add previous semester grades
		termmax = data.termnum.max()
		termmin = data.termnum.min()
		for t in np.arange(termmin + 1, termmax + 1):

			d = data[data.termnum == t -1].groupby('sid')[['grdpts']].mean()
			d.columns = ['grade_previous1']
			d['termnum'] = t
			data = pd.merge(data, d.reset_index(), on=['sid', 'termnum'], how='left')
			data.loc[data.termnum == t, 'grade_previous'] = data['grade_previous1']
			data.drop('grade_previous1', axis=1, inplace=True)
			
		# course features
		data['instructor_avg'] = data.groupby('iid').grdpts.transform("mean")
		
		# add categorical dummies
		cat_vars = DUMMYVAR
		cat_names_list = []
		for var in cat_vars:
			cat_list='var' + '_' + var
			cat_list = pd.get_dummies(data[var], prefix=var)
			data = data.join(cat_list)
			
		self.data = data
		return data
		
			
if __name__ == '__main__':		
	output_path = sys.argv[1]
	if not os.path.exists(output_path):
		print("output path, %s doesn't exist!" %output_path)
		sys.exit(1)
		
	input_path= sys.argv[2]
	if not os.path.exists(input_path):
		print("input path, %s doesn't exist!" %input_path)
		sys.exit(1)
		
	dset = dataset(input_path)
	data = dset.map_col('all')
	
data.to_csv(os.path.join(output_path, 'preprocessed_students_fl_all.csv'))