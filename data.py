import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


courses = pd.read_csv('C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_courses3.csv',low_memory=False)
degrees = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_degrees3.csv",low_memory=False)


sample = degrees[(degrees['degmaj1'].isin(['CS']) == True) | (degrees['degmaj1'].isin(['ACS']) == True)]
#use isin==True to get all CS and ACS degrees
sample = sample.dropna(axis=1,how='all')
#drop columns with ALL NA's
sample = sample.fillna("None")
#fill NA's with None (no major)
sample = sample.reset_index(drop=True)
#reset the indicies of the whole dataframe for easier analysis
sample['id'] = sample['id'].astype(int)
#cast the id values as int (Python automatically casts them as float for some reason)

'''the above script gets all the CS/ACS majors into 1 dataframe, then cleans up any NaN values'''

'''
x = courses["grdpts"].where(courses['DISC'] == 'MATH')
x = x.dropna()
plt.ylabel("Cumulative Math Grades for 2016")
plt.hist(x)
plt.show()
#histogram
'''