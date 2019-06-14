import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

degrees2015 = pd.read_csv('REU2015/nsf_degrees12.csv',low_memory=False) 
student2015 = pd.read_csv('REU2015/nsf_student12.csv',low_memory=False)
demographics2015 = pd.read_csv('REU2015/nsf_demographics12.csv',low_memory=False)

#merge student and demographics
df3 = pd.merge(student2015, demographics2015, on = 'id', how = 'left')
df3.set_index('id',inplace = True)
df3.to_csv('MergedStudentDemographics2015.csv')
#end of csv conversion

#creates a new data frame with unique student IDs 
merged2015 = pd.read_csv('MergedStudentDemographics2015.csv',low_memory=False)
merged2015.drop_duplicates('id',inplace = True)

#counts the number of students with demographics
seriesObj = merged2015.apply(lambda x: True if ((x['race'] != None) & (x['SEX'] != None) & (x['ENTRY_AGE'] != None)) else false, axis = 1)
demogCount = len(seriesObj[seriesObj == True].index)
print('Total number of students with demographics is ', len(merged2015), '/', demogCount)
