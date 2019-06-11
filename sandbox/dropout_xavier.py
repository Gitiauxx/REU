import pandas as pd
import os

DATA_FILE = './../data/FTF'

degrees_2015 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_degrees2.csv'), low_memory=False)
degrees_2017 =  pd.read_csv(os.path.join(DATA_FILE, 'Fall2017/nsf_ftf_degrees4.csv'), low_memory=False)

# keep CS, ACS students only
cs_2015 = degrees_2015.loc[degrees_2015['degmaj1'].isin(['CS', 'ACS']), :]
cs_2017 = degrees_2017.loc[degrees_2017['degmaj1'].isin(['CS', 'ACS']), :]

# it shows that degrees_2017 contain all students that have graduated up to 2017 (so contains all students in cs_2015) 
assert len(cs_2015.loc[~cs_2015.id.isin(cs_2017.id), :])   == 0

# dropout: students that show up in the students files in 2015 but not in the students file / degree file in 2016
student2015 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_student2.csv'), low_memory=False)
student2015.drop_duplicates('id', inplace=True)

student2016 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2016/nsf_ftf_student3.csv'), low_memory=False)
student2016.drop_duplicates('id', inplace=True)

dropout = student2015.loc[(~student2015.id.isin(student2016.id)) & (~student2015.id.isin(degrees_2017.id)), ['cohort_pmajr']]
print(dropout)




