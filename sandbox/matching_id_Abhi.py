import pandas as pd

student2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_ftf_student2.csv", low_memory=False)
student2015.drop(columns="ACAD_STDNG",inplace=True)

student2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_student3.csv", low_memory=False)
student2016.drop(columns="ACAD_STDNG",inplace=True)

student2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_student4.csv", low_memory=False)
student2017.drop(columns="acad_stdng",inplace=True)

students_total = pd.concat([student2015,student2016,student2017])
students_total.drop_duplicates('id',inplace=True)

degrees_total_2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_degrees12.csv", low_memory=False)
degrees_total_2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_degrees3.csv", low_memory=False)
degrees_total_2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_degrees4.csv", low_memory=False)

degrees_total = pd.concat([degrees_total_2015,degrees_total_2016,degrees_total_2017])
degrees_total.drop_duplicates('id',inplace=True)

demographics_2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_demographics12.csv", low_memory=False)
demographics_2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_demographics3.csv", low_memory=False)
demographics_2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_demographics4.csv", low_memory=False)

demographics_total = pd.concat([demographics_2015,demographics_2016,demographics_2017])
demographics_total.drop_duplicates('id',inplace=True)

cohort_2009 = students_total[(students_total.cohort.isin(['200970'])==True) | (students_total.cohort.isin(['200910'])==True) | (students_total.cohort.isin(['200940'])==True)]
cohort_2010 = students_total[(students_total.cohort.isin(['201070'])==True) | (students_total.cohort.isin(['201010'])==True) | (students_total.cohort.isin(['201040'])==True)]
cohort_2011 = students_total[(students_total.cohort.isin(['201170'])==True) | (students_total.cohort.isin(['201110'])==True) | (students_total.cohort.isin(['201140'])==True)]

cohort_2012 = students_total[(students_total.cohort.isin(['201270'])==True) | (students_total.cohort.isin(['201210'])==True) | (students_total.cohort.isin(['201240'])==True)]
cohort_2013 = students_total[(students_total.cohort.isin(['201370'])==True) | (students_total.cohort.isin(['201310'])==True) | (students_total.cohort.isin(['201340'])==True)]
cohort_2014 = students_total[(students_total.cohort.isin(['201470'])==True) | (students_total.cohort.isin(['201410'])==True) | (students_total.cohort.isin(['201440'])==True)]


admissions_total = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_admissions12.csv", low_memory=False)
admissions_total = admissions_total.drop(["cohort","Entry_Student_Type","Permanent_Address_NATION","Permanent_Address_NATION_CODE","Score_Optional","HS_CEEB_Code"],axis=1)

admissions_2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_admissions3.csv", low_memory=False)
admissions_2016 = admissions_2016.drop(["cohort","Entry_Student_Type","Permanent_Address_NATION","Permanent_Address_NATION_CODE","Score_Optional","HS_CEEB_Code"],axis=1)

admissions_2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_admissions4.csv", low_memory=False)
admissions_2017 = admissions_2017.drop(["cohort","Entry_Student_Type","Permanent_Address_NATION","Permanent_Address_NATION_CODE","Score_Optional","HS_CEEB_Code"],axis=1)

admissions_total = pd.concat([admissions_total,admissions_2016,admissions_2017])
admissions_total.drop_duplicates('id',inplace=True)

'''
People who graduated from 2009 cohort
'''
cohort_2009_grad_2011 = degrees_total[(degrees_total.GRADTERM.isin([201110,201140,201170]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['200970','200910','200940'])==True)]
cohort_2009_grad_2012 = degrees_total[(degrees_total.GRADTERM.isin([201210,201240,201270]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['200970','200910','200940'])==True)]
cohort_2009_grad_2013 = degrees_total[(degrees_total.GRADTERM.isin([201310,201340,201370]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['200970','200910','200940'])==True)]
cohort_2009_grad_2014 = degrees_total[(degrees_total.GRADTERM.isin([201410,201440,201470]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['200970','200910','200940'])==True)]
cohort_2009_grad_2015 = degrees_total[(degrees_total.GRADTERM.isin([201510,201540,201570]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['200970','200910','200940'])==True)]
cohort_2009_grad_2016 = degrees_total[(degrees_total.GRADTERM.isin([201610,201640,201670]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['200970','200910','200940'])==True)]
cohort_2009_grad_2017 = degrees_total[(degrees_total.GRADTERM.isin([201710,201740,201770]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['200970','200910','200940'])==True)]

grad_2009_total = pd.concat([cohort_2009_grad_2011,cohort_2009_grad_2012,cohort_2009_grad_2013,cohort_2009_grad_2014,cohort_2009_grad_2015,cohort_2009_grad_2016,cohort_2009_grad_2017],axis=0,sort=True)
grad_2009_total = grad_2009_total.merge(admissions_total,on='id')
grad_2009_total.drop_duplicates('id', inplace=True)
grad_2009_total = pd.merge(grad_2009_total,demographics_total,on='id')

dropout_2009 = cohort_2009[(cohort_2009.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2009.id.isin(degrees_total.id)]
#dropout_2009.set_index("id",inplace=True) #make ID on the left side
dropout_2009 = pd.merge(dropout_2009,demographics_total,on='id')
dropout_2009 = dropout_2009.merge(admissions_total,on='id')
#who dropped in 2009

'''
People who graduated from 2010 cohort 
'''

cohort_2010_grad_2012 = degrees_total[(degrees_total.GRADTERM.isin([201210,201240,201270]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201070','201010','201040'])==True)]
cohort_2010_grad_2013 = degrees_total[(degrees_total.GRADTERM.isin([201310,201340,201370]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201070','201010','201040'])==True)]
cohort_2010_grad_2014 = degrees_total[(degrees_total.GRADTERM.isin([201410,201440,201470]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS"))) & (degrees_total.cohort.isin(['201070','201010','201040'])==True)]


cohort_2010_grad_2015 = degrees_total[(degrees_total.GRADTERM.isin([201510,201540,201570]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201070','201010','201040'])==True)]
cohort_2010_grad_2016 = degrees_total[(degrees_total.GRADTERM.isin([201610,201640,201670]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201070','201010','201040'])==True)]
cohort_2010_grad_2017 = degrees_total[(degrees_total.GRADTERM.isin([201710,201740,201770]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201070','201010','201040'])==True)]


grad_2010_total = pd.concat([cohort_2010_grad_2012,cohort_2010_grad_2013,cohort_2010_grad_2014,cohort_2010_grad_2015,cohort_2010_grad_2016,cohort_2010_grad_2017])
grad_2010_total = grad_2010_total.reset_index(drop=True)

grad_2010_total = grad_2010_total.merge(admissions_total,on='id')

dropout_2010 = cohort_2010[(cohort_2010.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2010.id.isin(degrees_total.id)]
dropout_2010 = pd.merge(dropout_2010,demographics_total,on='id')
dropout_2010 = dropout_2010.merge(admissions_total,on='id')
#who dropped in 2010

'''
People who graduated from 2011 cohort 
'''

test = degrees_total[degrees_total.GRADTERM.isin([201410]) & ((degrees_total.cohort.isin(['201170','201110','201140'])==True) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS")))]

cohort_2011_grad_2013 = degrees_total[(degrees_total.GRADTERM.isin([201310,201340,201370]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201170','201110','201140'])==True)]
cohort_2011_grad_2014 = degrees_total[(degrees_total.GRADTERM.isin([201410,201440,201470]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201170','201110','201140'])==True)]
cohort_2011_grad_2015 = degrees_total[(degrees_total.GRADTERM.isin([201510,201540,201570]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201170','201110','201140'])==True)]
cohort_2011_grad_2016 = degrees_total[(degrees_total.GRADTERM.isin([201610,201640,201670]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201170','201110','201140'])==True)]
cohort_2011_grad_2017 = degrees_total[(degrees_total.GRADTERM.isin([201710,201740,201770]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201170','201110','201140'])==True)]

grad_2011_total = pd.concat([cohort_2011_grad_2013,cohort_2011_grad_2014,cohort_2011_grad_2015,cohort_2011_grad_2016,cohort_2011_grad_2017])
grad_2011_total = grad_2011_total.reset_index(drop=True)
#difference = set(grad_2011_total.columns).symmetric_difference(dropbox.columns)

grad_2011_total = pd.merge(grad_2011_total,demographics_total,on='id')
grad_2011_total = grad_2011_total.merge(admissions_total,on='id')

dropout_2011 = cohort_2011[(cohort_2011.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2011.id.isin(degrees_total.id)]
dropout_2011 = pd.merge(dropout_2011,demographics_total,on='id')
dropout_2011 = dropout_2011.merge(admissions_total,on='id')


'''
People who graduated from 2012 cohort
'''
cohort_2012_grad_2014 = degrees_total[(degrees_total.GRADTERM.isin([201410,201440,201470]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201270','201210','201240'])==True)]
cohort_2012_grad_2015 = degrees_total[(degrees_total.GRADTERM.isin([201510,201540,201570]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201270','201210','201240'])==True)]
cohort_2012_grad_2016 = degrees_total[(degrees_total.GRADTERM.isin([201610,201640,201670]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201270','201210','201240'])==True)]
cohort_2012_grad_2017 = degrees_total[(degrees_total.GRADTERM.isin([201710,201740,201770]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201270','201210','201240'])==True)]

grad_2012_total = pd.concat([cohort_2012_grad_2014,cohort_2012_grad_2015,cohort_2012_grad_2016,cohort_2012_grad_2017],axis=0,sort=True)
grad_2012_total = pd.merge(grad_2012_total,demographics_total,on='id')
grad_2012_total = grad_2012_total.merge(admissions_total,on='id')

dropout_2012 = cohort_2012[(cohort_2012.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2012.id.isin(degrees_total.id)]
dropout_2012 = pd.merge(dropout_2012,demographics_total,on='id')
dropout_2012 = dropout_2012.merge(admissions_total,on='id')

'''
 People who graduated from 2013 cohort
'''
cohort_2013_grad_2015 = degrees_total[(degrees_total.GRADTERM.isin([201510,201540,201570]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201370','201310','201340'])==True)]
cohort_2013_grad_2016 = degrees_total[(degrees_total.GRADTERM.isin([201610,201640,201670]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201370','201310','201340'])==True)]
cohort_2013_grad_2017 = degrees_total[(degrees_total.GRADTERM.isin([201710,201740,201770]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201370','201310','201340'])==True)]

grad_2013_total = pd.concat([cohort_2013_grad_2015,cohort_2013_grad_2016,cohort_2013_grad_2017],axis=0,sort=True)
grad_2013_total = pd.merge(grad_2013_total,demographics_total,on='id')
grad_2013_total = grad_2013_total.merge(admissions_total,on='id')

dropout_2013 = cohort_2013[(cohort_2013.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2013.id.isin(degrees_total.id)]
dropout_2013 = pd.merge(dropout_2013,demographics_total,on='id')
dropout_2013 = dropout_2013.merge(admissions_total,on='id')

'''
 People who graduated from 2014 cohort
'''
cohort_2014_grad_2016 = degrees_total[(degrees_total.GRADTERM.isin([201610,201640,201670]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201470','201410','201440'])==True)]
cohort_2014_grad_2017 = degrees_total[(degrees_total.GRADTERM.isin([201710,201740,201770]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201470','201410','201440'])==True)]

grad_2014_total = pd.concat([cohort_2014_grad_2016,cohort_2014_grad_2017],axis=0,sort=True)
grad_2014_total = pd.merge(grad_2014_total,demographics_total,on='id')
grad_2014_total = grad_2014_total.merge(admissions_total,on='id')

dropout_2014 = cohort_2014[(cohort_2014.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2014.id.isin(degrees_total.id)]
dropout_2014 = pd.merge(dropout_2014,demographics_total,on='id')
dropout_2014 = dropout_2014.merge(admissions_total,on='id')


grad_export = pd.concat([grad_2009_total,grad_2010_total,grad_2011_total,grad_2012_total,grad_2013_total,grad_2014_total],axis=0,sort=True)

#dropbox['id']=dropbox.index
#dropbox = dropbox.reset_index(drop=True)

grad_export['cohort_year'] = grad_export.cohort.apply(lambda x: int(str(x)[:4]))
print(grad_export.groupby('cohort_year').size())
exit(2)

'''
grad_export = grad_export.reset_index(drop=True)
grad_export.set_index("id",inplace=True)
grad_export['dropout']=0
grad_export.drop(columns="DEGREE",inplace=True)
grad_export.drop(columns="GRADTERM",inplace=True)
grad_export.drop(columns="PDEG",inplace=True)
grad_export.drop(columns="cumgpa2",inplace=True)
grad_export.drop(columns="degcoll",inplace=True)
grad_export.drop(columns="degmaj1",inplace=True)
grad_export.drop(columns="degmaj2",inplace=True)
grad_export.drop(columns="degminor1",inplace=True)
grad_export.drop(columns="degminor2",inplace=True)
grad_export.drop(columns="termgpa2",inplace=True)
grad_export.to_csv(r"/Users/abhi/Documents/REU/grad_removed_columns.csv")
exit(2)
'''


'''all students who have graduated from CS/ACS'''

'''
export_dropouts = pd.concat([dropout_2009,dropout_2010,dropout_2011,dropout_2012,dropout_2013],axis=0,sort=True)
#export_dropouts = export_dropouts.reset_index(drop=True)
export_dropouts.set_index("id",inplace=True)
export_dropouts['dropout']=1
#export_dropouts.to_csv(r"C:\\Users\\Pam\\Documents\\REU\\DropoutCS_Demographics_Students_Degrees_Admissions.csv")
#all students who have dropped from CS/ACS'''
'''


#degrees_total[degrees_total.id.isin(cohort_2012.id) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))]
#cohort_2012_grad_2016 = degrees_total[~degrees_total.id.isin(cohort_2012_grad_2015.id) & degrees_total.id.isin(cohort_2012.id) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))]
#cohort_2012_grad_2016 = cohort_2012_grad_2016.reset_index(drop=True)

#cohort_2012_grad_2017 = degrees_total[degrees_total.id.isin(cohort_2012.id) & (~degrees_total.id.isin(cohort_2012_grad_2016.id)) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))]
#cohort_2012_grad_2017 = cohort_2012_grad_2017.reset_index(drop=True)
#cohort_2013_grad_2016 = degrees_total[~degrees_total.id.isin(cohort_2012_grad_2015.id) & ~degrees_total.id.isin(cohort_2012_grad_2016.id) & degrees_total.id.isin(cohort_2013.id) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))]

#cohort_2013_grad_2016 = degrees_total[degrees_total.id.isin(cohort_2013.id) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))]
#cohort_2013_grad_2016 = degrees_total[degrees_total.GRADTERM.isin([201610,201640,201670]) & degrees_total.id.isin(cohort_2013.id) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))]

#cohort_2013_grad_2017 = degrees_total[~degrees_total.id.isin(cohort_2013_grad_2016.id) & degrees_total.id.isin(cohort_2013.id) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))]
#print(cohort_2013_grad_2017.__len__())
#print(degrees_total.GRADTERM==201510,201540,201570)
'''
#cohort_2012_grad_2015 = degrees_total[degrees_total.GRADTERM.isin([201510,201540,201570]) & degrees_total.id.isin(cohort_2012.id) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))]