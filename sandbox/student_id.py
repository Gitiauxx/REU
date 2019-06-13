import pandas as pd
import os
import numpy as np

DATA_FILE = './../data/FTF'

# students data
s1 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_student2.csv'), usecols=['id'], low_memory=False)
s2 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2016/nsf_ftf_student3.csv'), usecols=['id'], low_memory=False)
s3 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2017/nsf_ftf_student4.csv'), usecols=['id'], low_memory=False)

student = pd.concat([s1, s2, s3]).drop_duplicates('id').set_index('id')
print(len(student))

# demographics
d0 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_demographics12.csv'), low_memory=False)
d1 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2015/nsf_ftf_demographics2.csv'), low_memory=False)
d2 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2016/nsf_ftf_demographics3.csv'), low_memory=False)
d3 = pd.read_csv(os.path.join(DATA_FILE, 'Fall2017/nsf_ftf_demographics4.csv'), low_memory=False)
demo = pd.concat([d0, d1, d2, d3]).drop_duplicates('id').set_index('id')
print(len(demo))

# how many can we merge?
demo_student = student.join(demo, how='left')
print(len(demo_student[(~np.isnan(demo_student.ENTRY_AGE))]))