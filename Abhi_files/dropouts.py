import pandas as pd


student2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_ftf_student2.csv", usecols=['id', 'cohort', 'PMAJR','TERMBNR'])
#student2015.drop(columns="ACAD_STDNG",inplace=True)

student2015_1 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_student12.csv", usecols=['id', 'cohort', 'PMAJR','TERMBNR'])
#student2015_1.drop(columns="ACAD_STDNG",inplace=True)

student2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_student3.csv", usecols=['id', 'cohort', 'PMAJR','TERMBNR'])
#student2016.drop(columns="ACAD_STDNG",inplace=True)

student2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_student4.csv", usecols=['id', 'cohort', 'PMAJR','TERMBNR'])
#student2017.drop(columns="acad_stdng",inplace=True)

students_total = pd.concat([student2015,student2016,student2017,student2015_1],axis=0,sort=True)
#students_total.drop_duplicates('id',inplace=True)

degrees_total_2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_degrees12.csv", low_memory=False)
degrees_total_2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_degrees3.csv", low_memory=False)
degrees_total_2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_degrees4.csv", low_memory=False)

degrees_total = pd.concat([degrees_total_2015,degrees_total_2016,degrees_total_2017],axis=0,sort=True)
degrees_total.drop_duplicates('id',inplace=True)

demographics_2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_demographics12.csv", low_memory=False)
demographics_2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_demographics3.csv", low_memory=False)
demographics_2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_demographics4.csv", low_memory=False)

demographics_total = pd.concat([demographics_2015,demographics_2016,demographics_2017],axis=0,sort=True)
demographics_total.drop_duplicates('id',inplace=True)

cohort_2009 = students_total[(students_total.cohort.isin(['200970'])==True) | (students_total.cohort.isin(['200910'])==True) | (students_total.cohort.isin(['200940'])==True)]
cohort_2010 = students_total[(students_total.cohort.isin(['201070'])==True) | (students_total.cohort.isin(['201010'])==True) | (students_total.cohort.isin(['201040'])==True)]
cohort_2011 = students_total[(students_total.cohort.isin(['201170'])==True) | (students_total.cohort.isin(['201110'])==True) | (students_total.cohort.isin(['201140'])==True)]

cohort_2012 = students_total[(students_total.cohort.isin(['201270'])==True) | (students_total.cohort.isin(['201210'])==True) | (students_total.cohort.isin(['201240'])==True)]
cohort_2013 = students_total[(students_total.cohort.isin(['201370'])==True) | (students_total.cohort.isin(['201310'])==True) | (students_total.cohort.isin(['201340'])==True)]
cohort_2014 = students_total[(students_total.cohort.isin(['201470'])==True) | (students_total.cohort.isin(['201410'])==True) | (students_total.cohort.isin(['201440'])==True)]

dropouts = students_total[students_total.PMAJR.isin(['CS','ACS']) & ~students_total.id.isin(degrees_total.id)]
dropouts = dropouts[~dropouts.TERMBNR.isin(['200940','201040','201140','201240','201340','201440','201540','201640','201740'])]
dropouts.sort_values(['id','TERMBNR','cohort'],inplace=True)
dropouts = dropouts.groupby(['id','TERMBNR','cohort']).size().reset_index()
print("2")