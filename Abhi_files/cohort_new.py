import pandas as pd

student2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_ftf_student2.csv", low_memory=False)
student2015.drop(columns="ACAD_STDNG",inplace=True)

student2015_1 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_student12.csv", low_memory=False)
student2015_1.drop(columns="ACAD_STDNG",inplace=True)

student2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_student3.csv", low_memory=False)
student2016.drop(columns="ACAD_STDNG",inplace=True)

student2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_student4.csv", low_memory=False)
student2017.drop(columns="acad_stdng",inplace=True)

student2018 = pd.read_sas("/Users/abhi/Dropbox/original/Additional Files Fall 2018/nsf_ftf_student5.sas7bdat", encoding='latin-1')
student2018.drop(columns="acad_stdng",inplace=True)

students_total = pd.concat([student2015,student2016,student2017,student2015_1,student2018],axis=0,sort=True)
students_total.drop_duplicates('id',inplace=True)

degrees_total_2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_degrees12.csv", low_memory=False)
degrees_total_2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_degrees3.csv", low_memory=False)
degrees_total_2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_degrees4.csv", low_memory=False)
degrees_total_2018 = pd.read_sas("/Users/abhi/Dropbox/original/Additional Files Fall 2018/nsf_ftf_degrees5.sas7bdat",encoding='latin-1')

degrees_total = pd.concat([degrees_total_2015,degrees_total_2016,degrees_total_2017,degrees_total_2018],axis=0,sort=True)
degrees_total.drop_duplicates('id',inplace=True)

demographics_2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_demographics12.csv", low_memory=False)
demographics_2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_demographics3.csv", low_memory=False)
demographics_2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_demographics4.csv", low_memory=False)
demographics_2018 = pd.read_sas("/Users/abhi/Dropbox/original/Additional Files Fall 2018/nsf_ftf_demographics5.sas7bdat",encoding='latin-1')

demographics_total = pd.concat([demographics_2015,demographics_2016,demographics_2017],axis=0,sort=True)
demographics_total.drop_duplicates('id',inplace=True)

admissions_2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_admissions12.csv", low_memory=False)
admissions_2015 = admissions_2015.drop(["cohort","Entry_Student_Type","Permanent_Address_NATION","Permanent_Address_NATION_CODE","Score_Optional","HS_CEEB_Code"],axis=1)

admissions_2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_admissions3.csv", low_memory=False)
admissions_2016 = admissions_2016.drop(["cohort","Entry_Student_Type","Permanent_Address_NATION","Permanent_Address_NATION_CODE","Score_Optional","HS_CEEB_Code"],axis=1)

admissions_2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_admissions4.csv", low_memory=False)
admissions_2017 = admissions_2017.drop(["cohort","Entry_Student_Type","Permanent_Address_NATION","Permanent_Address_NATION_CODE","Score_Optional","HS_CEEB_Code"],axis=1)

admissions_2018 = pd.read_sas("/Users/abhi/Dropbox/original/Additional Files Fall 2018/nsf_ftf_admissions5.sas7bdat", encoding='latin-1')
admissions_2018 = admissions_2018.drop(["cohort","Entry_Student_Type","Permanent_Address_NATION","Permanent_Address_NATION_CODE","Score_Optional","HS_CEEB_Code"],axis=1)

admissions_total = pd.concat([admissions_2015,admissions_2016,admissions_2017,admissions_2018])
admissions_total.drop_duplicates('id',inplace=True)

cohort_2009 = students_total[students_total.cohort.isin([200970,200910,200940])]
cohort_2010 = students_total[students_total.cohort.isin([201070,201010,201040])]
cohort_2011 = students_total[students_total.cohort.isin([201170,201110,201140])]

cohort_2012 = students_total[students_total.cohort.isin([201270,201210,201240])]
cohort_2013 = students_total[students_total.cohort.isin([201370,201310,201340])]
cohort_2014 = students_total[students_total.cohort.isin([201470,201410,201440])]

degrees_total.GRADTERM = degrees_total.GRADTERM.astype(int)
degrees_total.cohort = degrees_total.cohort.astype(int)


admissions_2015 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2015/nsf_admissions12.csv", low_memory=False)
admissions_2015 = admissions_2015.drop(["cohort","Entry_Student_Type","Permanent_Address_NATION","Permanent_Address_NATION_CODE","Score_Optional","HS_CEEB_Code"],axis=1)

admissions_2016 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2016/nsf_ftf_admissions3.csv", low_memory=False)
admissions_2016 = admissions_2016.drop(["cohort","Entry_Student_Type","Permanent_Address_NATION","Permanent_Address_NATION_CODE","Score_Optional","HS_CEEB_Code"],axis=1)

admissions_2017 = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_admissions4.csv", low_memory=False)
admissions_2017 = admissions_2017.drop(["cohort","Entry_Student_Type","Permanent_Address_NATION","Permanent_Address_NATION_CODE","Score_Optional","HS_CEEB_Code"],axis=1)

admissions_total = pd.concat([admissions_2015,admissions_2016,admissions_2017])
admissions_total.drop_duplicates('id',inplace=True)

'''
People who graduated from 2009 cohort
'''
year_2009 = [200970,200910,200940]
year_2010 = [201070,201010,201040]
year_2011 = [201110,201140,201170]
year_2012 = [201210,201240,201270]
year_2013 = [201310,201340,201370]
year_2014 = [201410,201440,201470]
year_2015 = [201510,201540,201570]
year_2016 = [201610,201640,201670]
year_2017 = [201710,201740,201770]
deg_majors = ['CS','ACS']


degree_cohort_2009 = degrees_total.cohort.isin(year_2009)
degree_cohort_2010 = degrees_total.cohort.isin(year_2010)
degree_cohort_2011 = degrees_total.cohort.isin(year_2011)
degree_cohort_2012 = degrees_total.cohort.isin(year_2012)
degree_cohort_2013 = degrees_total.cohort.isin(year_2013)
degree_cohort_2014 = degrees_total.cohort.isin(year_2014)
degree_cohort_2015 = degrees_total.cohort.isin(year_2015)
degree_cohort_2016 = degrees_total.cohort.isin(year_2016)
degree_cohort_2017 = degrees_total.cohort.isin(year_2017)

grad_2011 = degrees_total.GRADTERM.isin(year_2011)
grad_2012 = degrees_total.GRADTERM.isin(year_2012)
grad_2013 = degrees_total.GRADTERM.isin(year_2013)
grad_2014 = degrees_total.GRADTERM.isin(year_2014)
grad_2015 = degrees_total.GRADTERM.isin(year_2015)
grad_2016 = degrees_total.GRADTERM.isin(year_2016)
grad_2017 = degrees_total.GRADTERM.isin(year_2017)

deg_major1 = degrees_total.degmaj1.isin(deg_majors)
deg_major2 = degrees_total.degmaj2.isin(deg_majors)



cohort_2009_grad_2011 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2009 & grad_2011)]
cohort_2009_grad_2012 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2009 & grad_2012)]
cohort_2009_grad_2013 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2009 & grad_2013)]
cohort_2009_grad_2014 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2009 & grad_2014)]

cohort_2009_grad_2015 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2009 & grad_2015)]
cohort_2009_grad_2016 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2009 & grad_2016)]
cohort_2009_grad_2017 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2009 & grad_2017)]

grad_2009_total = pd.concat([cohort_2009_grad_2011,cohort_2009_grad_2012,cohort_2009_grad_2013], axis=0, sort=True)

#dropout_2009 = cohort_2009[(cohort_2009.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2009.id.isin(degrees_total.id)]

dropout_2009 = cohort_2009[cohort_2009.cohort_pmajr.isin(deg_majors) & ~cohort_2009.id.isin(grad_2009_total.id)]


#who dropped in 2009

'''
People who graduated from 2010 cohort 
'''


cohort_2010_grad_2012 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2010 & grad_2012)]
cohort_2010_grad_2013 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2010 & grad_2013)]
cohort_2010_grad_2014 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2010 & grad_2014)]

cohort_2010_grad_2015 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2010 & grad_2015)]
cohort_2010_grad_2016 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2010 & grad_2016)]
cohort_2010_grad_2017 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2010 & grad_2017)]

grad_2010_total = pd.concat([cohort_2010_grad_2012,cohort_2010_grad_2013,cohort_2010_grad_2014],axis=0,sort=True) #cohort_2010_grad_2015,cohort_2010_grad_2016,cohort_2010_grad_2017])
grad_2010_total = grad_2010_total.reset_index(drop=True)

#dropout_2010 = cohort_2010[(cohort_2010.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2010.id.isin(degrees_total.id)]

dropout_2010 = cohort_2010[(cohort_2010.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2010.id.isin(grad_2010_total.id)]



#who dropped in 2010

'''
People who graduated from 2011 cohort 
'''



cohort_2011_grad_2013 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2011 & grad_2013)]
cohort_2011_grad_2014 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2011 & grad_2014)]
cohort_2011_grad_2015 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2011 & grad_2015)]

cohort_2011_grad_2016 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2011 & grad_2016)]
cohort_2011_grad_2017 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2011 & grad_2017)]

grad_2011_total = pd.concat([cohort_2011_grad_2013,cohort_2011_grad_2014,cohort_2011_grad_2015],axis=0,sort=True) #cohort_2011_grad_2016,cohort_2011_grad_2017])
grad_2011_total = grad_2011_total.reset_index(drop=True)

#dropout_2011 = cohort_2011[(cohort_2011.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2011.id.isin(degrees_total.id)]

dropout_2011 = cohort_2011[(cohort_2011.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2011.id.isin(grad_2011_total.id)]


'''
People who graduated from 2012 cohort
'''


cohort_2012_grad_2014 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2012 & grad_2014)]
cohort_2012_grad_2015 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2012 & grad_2015)]
cohort_2012_grad_2016 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2012 & grad_2016)]
cohort_2012_grad_2017 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2012 & grad_2017)]

grad_2012_total = pd.concat([cohort_2012_grad_2014,cohort_2012_grad_2015,cohort_2012_grad_2016],axis=0,sort=True)#cohort_2012_grad_2017],axis=0,sort=True)

#dropout_2012 = cohort_2012[(cohort_2012.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2012.id.isin(degrees_total.id)]

dropout_2012 = cohort_2012[(cohort_2012.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2012.id.isin(grad_2012_total.id)]



'''
 People who graduated from 2013 cohort
'''
cohort_2013_grad_2015 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2013 & grad_2015)]
cohort_2013_grad_2016 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2013 & grad_2016)]
cohort_2013_grad_2017 = degrees_total[(deg_major1 | deg_major2) & (degree_cohort_2013 & grad_2017)]

grad_2013_total = pd.concat([cohort_2013_grad_2015,cohort_2013_grad_2016,cohort_2013_grad_2017],axis=0,sort=True)

#dropout_2013 = cohort_2013[(cohort_2013.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2013.id.isin(degrees_total.id)]
#dropout_2013 = cohort_2013[(cohort_2013.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2013.id.isin(grad_2013_total.id)]

dropout_2013 = cohort_2013[(cohort_2013.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2013.id.isin(grad_2013_total.id)]



'''
 People who graduated from 2014 cohort
'''
cohort_2014_grad_2016 = degrees_total[(degrees_total.GRADTERM.isin([201610,201640,201670]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201470','201410','201440'])==True)]
cohort_2014_grad_2017 = degrees_total[(degrees_total.GRADTERM.isin([201710,201740,201770]) & ((degrees_total.degmaj1=="CS") | (degrees_total.degmaj1=="ACS") | (degrees_total.degmaj2=="CS"))) & (degrees_total.cohort.isin(['201470','201410','201440'])==True)]

#grad_2014_total = pd.concat([cohort_2014_grad_2016,cohort_2014_grad_2017],axis=0,sort=True)

#dropout_2014 = cohort_2014[(cohort_2014.cohort_pmajr.isin(['CS','ACS'])==True) & ~cohort_2014.id.isin(grad_2014_total)]

grad_export = pd.concat([grad_2009_total,grad_2010_total,grad_2011_total,grad_2012_total,grad_2013_total],axis=0,sort=True) #,grad_2014_total],axis=0,sort=True)
students_total = students_total.drop(["cohort","cohort_pmajr","cohort_pcoll"],axis=1)
grad_export = grad_export.merge(students_total,on='id')
grad_export = grad_export.merge(demographics_total,on='id')
grad_export = grad_export.merge(admissions_total,on='id')


grad_export = grad_export.reset_index(drop=True)
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

grad_export['cohort_year'] = grad_export.cohort.apply(lambda x: int(str(x)[:4]))
print(grad_export.groupby('cohort_year').size())

#grad_export.to_csv(r"/Users/abhi/Documents/REU/grad_removed_columns.csv")

#exit(2)

#all students who have graduated from CS/ACS


export_dropouts = pd.concat([dropout_2009,dropout_2010,dropout_2011,dropout_2012,dropout_2013],axis=0,sort=True)
export_dropouts = export_dropouts.reset_index(drop=True)

export_dropouts = export_dropouts.merge(demographics_total,on='id')
export_dropouts = export_dropouts.merge(admissions_total,on='id')
export_dropouts['dropout']=1
export_final = grad_export.append(export_dropouts)[grad_export.columns.tolist()]
export_final.drop(columns="Military_Status",inplace=True)
export_final.drop(columns="TOEFL_Paper",inplace=True)
export_final.drop(columns="TOEFL_Internet",inplace=True)
export_final.drop(columns="TOEFL_Convert_Paper",inplace=True)
export_final.drop(columns=["ACT_Composite","HS_Name","ACT_English","ACT_Reading","ACT_Math","ACT_Science"],inplace=True)

export_final = export_final.dropna(how='any')
export_final.drop_duplicates('id',inplace=True)
export_final.set_index('id',inplace=True)

export_dropouts['cohort_year'] = export_dropouts.cohort.apply(lambda x: int(str(x)[:4]))
print(export_dropouts.groupby('cohort_year').size())


#export_final.to_csv(r"/Users/abhi/Documents/REU/Final_Merged.csv")


exit(2)
