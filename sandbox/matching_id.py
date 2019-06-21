import pandas as pd
import os


DATA_FILE = './../data/FTF'

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
d_s['cohort_year'] = d_s.cohort.apply(lambda x: int(str(x)[:4]))
print(d_s.groupby('cohort_year').size())

# for CS/ACS students
print(d_s[d_s.degmaj1.isin(['CS', "ACS"])].groupby('cohort_year').size())