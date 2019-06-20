import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

courses2015 = pd.read_csv('REU2015/nsf_courses12.csv',low_memory=False) 
degrees2015 = pd.read_csv('REU2015/nsf_degrees12.csv',low_memory=False) 
student2015 = pd.read_csv('REU2015/nsf_student12.csv',low_memory=False)
demographics2015 = pd.read_csv('REU2015/nsf_demographics12.csv',low_memory=False)
admissions2015 = pd.read_csv('REU2015/nsf_demographics12.csv',low_memory=False)

graduated = pd.merge(degrees2015, admissions2015, on = 'id', how = 'left')
graduated.set_index('id',inplace = True)
#checks if (cohort is in 2009) & (GRADTERM is in 2013) & (degree graduates is CS or ACS) & (cohort major is CS or ACS)
graduated = graduated[((graduated['cohort'].astype(str).str.contains('2009')) == True) & ((graduated['GRADTERM'].astype(str).str.contains('2013')) == True) & ((graduated.degmaj1.isin(['CS'])==True) | (graduated.degmaj1.isin(['ACS'])==True)) & ((graduated.cohort_pmajr.isin(['CS'])==True) | (graduated.cohort_pmajr.isin(['ACS'])==True))]
graduated.to_csv('Graduated2013.csv')

print(graduated)
