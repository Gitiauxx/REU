'''
import pandas as pd
import os


DATA_FILE = '/Users/abhi/Dropbox/Data/FTF'

# degrees
degrees0 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_degrees12.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees_1 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_degrees2.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees_2 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_degrees2.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees_3 =  pd.read_csv(os.path.join(DATA_FILE, 'Fall2017/nsf_ftf_degrees4.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees = pd.concat([degrees0, degrees_2, degrees_1, degrees_3]) # .set_index was here based on 'id' if that needs to be implemented again
#degrees.drop_duplicates('id',inplace=True)

#students
s1 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_student2.csv'), usecols=['id'], low_memory=False)
s2 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2016/nsf_ftf_student3.csv'), usecols=['id'], low_memory=False)
s3 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2017/nsf_ftf_student4.csv'), usecols=['id'], low_memory=False)

student = pd.concat([s1, s2, s3]).drop_duplicates('id') #set_index() was set to 'id' here as well
# degrees-student
d_s = degrees.join(student, how='inner') #inner returns only the rows in which the left table (degrees) has matching keys in the right table (student)

# count by cohort
d_s['cohort_year'] = d_s.cohort.apply(lambda x: int(str(x)[:4]))
print(d_s.groupby('cohort_year').size())


#dropbox = d_s[(d_s.degmaj1.isin(['CS', "ACS"]) & (d_s.cohort.isin(['201070','201010','201040']))) & (d_s.GRADTERM.isin([201410,201440,201470]))]
# for CS/ACS students
#dropbox_2 = d_s[d_s.degmaj1.isin(['CS', "ACS"])]
test_dataframe = d_s[d_s.degmaj1.isin(['CS', "ACS"])]
print(d_s[d_s.degmaj1.isin(['CS', "ACS"])].groupby('cohort_year').size())
'''

import pandas as pd
import os


DATA_FILE = '/Users/abhi/Dropbox/Data/FTF'


# degrees
degrees0 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_degrees12.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees_1 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_degrees2.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees_2 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_degrees2.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees_3 =  pd.read_csv(os.path.join(DATA_FILE, 'Fall2017/nsf_ftf_degrees4.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees = pd.concat([degrees0, degrees_2, degrees_1, degrees_3]).drop_duplicates('id').set_index('id')


#students
s0 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_student12.csv'), usecols=['id', 'PMAJR'], low_memory=False)
s1 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_student2.csv'), usecols=['id', 'PMAJR'], low_memory=False)
s2 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2016/nsf_ftf_student3.csv'), usecols=['id', 'PMAJR'], low_memory=False)
s3 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2017/nsf_ftf_student4.csv'), usecols=['id', 'PMAJR'], low_memory=False)

student = pd.concat([s0, s1, s2, s3]).drop_duplicates('id').set_index('id')

# degrees-student
d_s = degrees.join(student, how='inner')

# count by cohort
d_s['cohort_year'] = d_s.cohort.apply(lambda x: int(str(x)[:4]))
#print(d_s.groupby('cohort_year').size())

# for CS/ACS students
#print(d_s[d_s.degmaj1.isin(['CS', "ACS"])].groupby('cohort_year').size())

# look at students that graduated within 4 years
d_s['graduation_year'] = d_s.GRADTERM.apply(lambda x: int(str(x)[:4]))

#print(d_s[d_s.graduation_year - d_s.cohort_year <= 4].groupby('cohort_year').size())
#print(d_s[(d_s.graduation_year - d_s.cohort_year <= 4) & (d_s.degmaj1.isin(['CS', "ACS"]))].groupby('cohort_year').size())

# look at students without graduation
d_all = student.join(degrees, how='left')
d_all = d_all[~d_all.cohort.isnull()]
d_all['cohort_year'] = d_all.cohort.apply(lambda x: int(str(x)[:4]))
d_all['not_graduated'] = (d_all.GRADTERM.isnull()).astype('int32')
dropout = d_all[(d_all.PMAJR.isin(['CS', 'ACS'])) & (d_all.not_graduated == 1)]
#print(dropout.head())
#print(d_all[(d_all.not_graduated == 1)].groupby('cohort_year').size())
print(d_all[(d_all.PMAJR.isin(['CS', 'ACS'])) & (d_all.not_graduated == 1)].groupby('cohort_year').size())

'''
import pandas as pd
import os


DATA_FILE = '/Users/abhi/Dropbox/Data/FTF'

# degrees
degrees0 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_degrees12.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees_1 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_degrees2.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees_2 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_degrees2.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees_3 =  pd.read_csv(os.path.join(DATA_FILE, 'Fall2017/nsf_ftf_degrees4.csv'), usecols=['id', 'cohort', 'GRADTERM', 'degmaj1'])
degrees = pd.concat([degrees0, degrees_2, degrees_1, degrees_3]).drop_duplicates('id').set_index('id')


#students
s1 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_student2.csv'), usecols=['id'], low_memory=False)
s2 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2016/nsf_ftf_student3.csv'), usecols=['id'], low_memory=False)
s3 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2017/nsf_ftf_student4.csv'), usecols=['id'], low_memory=False)

student = pd.concat([s1, s2, s3]).drop_duplicates('id').set_index('id')

# degrees-student
d_s = degrees.join(student, how='inner')

# count by cohort
dropbox = d_s[(d_s.degmaj1.isin(['CS', "ACS"]) & (d_s.cohort.isin(['201170','201110','201140'])))] #& (d_s.GRADTERM.isin([201410,201440,201470]) | d_s.GRADTERM.isin([201410,201440,201470]) | d_s.GRADTERM.isin([201510,201540,201570]) | d_s.GRADTERM.isin([201310,201340,201370]))]
#dropbox = dropbox.reset_index(drop=True)
d_s['cohort_year'] = d_s.cohort.apply(lambda x: int(str(x)[:4]))
print(d_s.groupby('cohort_year').size())

# for CS/ACS students
print(d_s[d_s.degmaj1.isin(['CS', "ACS"])].groupby('cohort_year').size())
'''


