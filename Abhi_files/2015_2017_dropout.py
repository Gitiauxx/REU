import pandas as pd
import matplotlib.pyplot as plt

# dropout: students that show up in the students files in 2015 but not in the students file / degree file in 2016
demographics_2015 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2015\\nsf_demographics12.csv", low_memory=False)
demographics_2015.drop_duplicates('id',inplace=True)
'''
demographics_2016 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_demographics3.csv", low_memory=False)
demographics_2016.drop_duplicates('id',inplace=True)
demographics_2017 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2017\\nsf_ftf_demographics4.csv", low_memory=False)
demographics_2017.drop_duplicates('id',inplace=True)
'''

student2015 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2015\\nsf_ftf_student2.csv", low_memory=False)
student2015.drop_duplicates('id', inplace=True)

student2016 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_student3.csv", low_memory=False)
#student2016.drop_duplicates('id', inplace=True)

student2017 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2017\\nsf_ftf_student4.csv", low_memory=False)
#student2017.drop_duplicates('id', inplace=True)

degrees_2015 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2015\\nsf_ftf_degrees2.csv", low_memory=False)

dropout_2015 = student2015[(~student2015.id.isin(student2016.id)) & (~student2015.id.isin(student2017.id)) & ((student2015.PMAJR.isin(['CS'])==True) | (student2015.PMAJR.isin(['ACS'])==True))]
#statement checks for: 2015 student ID's that are NOT in 2016/2017 & CS/ACS
dropout_2015 = dropout_2015.reset_index(drop=True)

dropout_2016 = student2016[((student2016.PMAJR.isin(['CS'])==True) | (student2016.PMAJR.isin(['ACS'])==True)) & (~student2016.id.isin(student2017.id))]
#dropout_2016 = dropout_2016.reset_index(drop=True)

drop_out_demographics = demographics_2015[demographics_2015.id.isin(dropout_2015.id)]
drop_out_demographics = drop_out_demographics.reset_index(drop=True)

''''
demographics_2 = demographics_2016[demographics_2016.id.isin(dropout_2015.id)]
demographics_3 = demographics_2017[demographics_2017.id.isin(dropout_2015.id)]
demographics_2 = demographics_2016[demographics_2016.id.isin(dropout_2015.id) | demographics_2016.id.isin(dropout_2016.id)]
demographics_3 = demographics_2017[demographics_2017.id.isin(dropout_2015.id) | demographics_2017.id.isin(dropout_2016.id)]

demographics_2016 = demographics_2016
'''


#dropout = student2015[(~student2015.id.isin(student2016.id)) & (~student2015.id.isin(student2017.id))]
#CS_math_drop = degrees_2015[degrees_2015.id.isin(dropout.id)]
'''
x = CS_math_drop[["degmaj1","degmaj2","degminor1","degminor2"]].copy()
x = x.fillna(value=0)
x = x[~x.degmaj2.isin([0]) | ~x.degminor1.isin([0]) | ~x.degminor2.isin([0])]
x = x.reset_index(drop=True)
'''
#plt.ylabel("Cumulative Math Grades for 2016")
#plt.hist(x)
#plt.show()
#PMAJR


'''
CS_math = degrees_2015[degrees_2015.degmaj1.isin(["CS"]) & (degrees_2015.degminor1.isin(["MATH"]) | degrees_2015.degmaj2.isin(["MATH"]))]
CS_math_drop = degrees_2015[degrees_2015.id.isin(dropout.id) & (degrees_2015.degminor1.isin(["MATH"]) | degrees_2015.degmaj2.isin(["MATH"]))]
CS_math_drop = CS_math_drop.reset_index(drop=True)
#do students with CS & Math double major/minors drop out at a greater frequency
#turns out, 3 out of 4 of the CS & Math double major/minors dropped out 
'''