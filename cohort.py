import pandas as pd

student2015 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2015\\nsf_student12.csv", low_memory=False)
student2015.drop_duplicates('id', inplace=True)

student2016 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_student3.csv", low_memory=False)
student2016.drop_duplicates('id', inplace=True)

student2017 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2017\\nsf_ftf_student4.csv", low_memory=False)
student2017.drop_duplicates('id', inplace=True)

degrees_2015 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2015\\nsf_ftf_degrees2.csv", low_memory=False)
degrees_2015.drop_duplicates('id', inplace=True)

degrees_2016 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_degrees3.csv", low_memory=False)
degrees_2016.drop_duplicates('id', inplace=True)

degrees_2017 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2017\\nsf_ftf_degrees4.csv", low_memory=False)
degrees_2017.drop_duplicates('id',inplace=True)

cohort_2009 = student2015[(student2015.cohort.isin(['200970'])==True) | (student2015.cohort.isin(['200910'])==True) | (student2015.cohort.isin(['200940'])==True)]
cohort_2010 = student2015[(student2015.cohort.isin(['201070'])==True) | (student2015.cohort.isin(['201010'])==True) | (student2015.cohort.isin(['201040'])==True)]
cohort_2011 = student2015[(student2015.cohort.isin(['201170'])==True) | (student2015.cohort.isin(['201110'])==True) | (student2015.cohort.isin(['201140'])==True)]

cohort_2012 = student2015[(student2015.cohort.isin(['201270'])==True) | (student2015.cohort.isin(['201210'])==True) | (student2015.cohort.isin(['201240'])==True)]
cohort_2013 = student2015[(student2015.cohort.isin(['201370'])==True) | (student2015.cohort.isin(['201310'])==True) | (student2015.cohort.isin(['201340'])==True)]
cohort_2014 = student2015[(student2015.cohort.isin(['201470'])==True) | (student2015.cohort.isin(['201410'])==True) | (student2015.cohort.isin(['201440'])==True)]

'''
People who graduated from 2009 cohort
'''
cohort_2009_grad_2011 = degrees_2015[degrees_2015.GRADTERM.isin([201110,201140,201170]) & degrees_2015.id.isin(cohort_2009.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2009_grad_2012 = degrees_2015[degrees_2015.GRADTERM.isin([201210,201240,201270]) & degrees_2015.id.isin(cohort_2009.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2009_grad_2013 = degrees_2015[degrees_2015.GRADTERM.isin([201310,201340,201370]) & degrees_2015.id.isin(cohort_2009.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2009_grad_2014 = degrees_2015[degrees_2015.GRADTERM.isin([201410,201440,201470]) & degrees_2015.id.isin(cohort_2009.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2009_grad_2015 = degrees_2015[degrees_2015.GRADTERM.isin([201510,201540,201570]) & degrees_2015.id.isin(cohort_2009.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2009_grad_2016 = degrees_2016[degrees_2016.GRADTERM.isin([201610,201640,201670]) & degrees_2016.id.isin(cohort_2009.id) & ((degrees_2016.degmaj1=="CS") | (degrees_2016.degmaj1=="ACS") | (degrees_2016.degmaj2=="CS"))]
cohort_2009_grad_2017 = degrees_2017[degrees_2017.GRADTERM.isin([201710,201740,201770]) & degrees_2017.id.isin(cohort_2009.id) & ((degrees_2017.degmaj1=="CS") | (degrees_2017.degmaj1=="ACS") | (degrees_2017.degmaj2=="CS"))]

dropout_2009 = cohort_2009[(cohort_2009.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2009.id.isin(degrees_2017.id)]
#who dropped in 2009
#important to put parenthesis around ==, or else & gets evaluated first

'''
People who graduated from 2010 cohort 
'''
cohort_2010_grad_2012 = degrees_2015[degrees_2015.GRADTERM.isin([201210,201240,201270]) & degrees_2015.id.isin(cohort_2010.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2010_grad_2013 = degrees_2015[degrees_2015.GRADTERM.isin([201310,201340,201370]) & degrees_2015.id.isin(cohort_2010.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2010_grad_2014 = degrees_2015[degrees_2015.GRADTERM.isin([201410,201440,201470]) & degrees_2015.id.isin(cohort_2010.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2010_grad_2015 = degrees_2015[degrees_2015.GRADTERM.isin([201510,201540,201570]) & degrees_2015.id.isin(cohort_2010.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2010_grad_2016 = degrees_2016[degrees_2016.GRADTERM.isin([201610,201640,201670]) & degrees_2016.id.isin(cohort_2010.id) & ((degrees_2016.degmaj1=="CS") | (degrees_2016.degmaj1=="ACS") | (degrees_2016.degmaj2=="CS"))]
cohort_2010_grad_2017 = degrees_2016[degrees_2016.GRADTERM.isin([201610,201640,201670]) & degrees_2016.id.isin(cohort_2010.id) & ((degrees_2016.degmaj1=="CS") | (degrees_2016.degmaj1=="ACS") | (degrees_2016.degmaj2=="CS"))]

dropout_2010 = cohort_2010[(cohort_2010.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2010.id.isin(degrees_2017.id)]
#who dropped in 2010

'''
People who graduated from 2011 cohort 
'''
cohort_2011_grad_2013 = degrees_2015[degrees_2015.GRADTERM.isin([201310,201340,201370]) & degrees_2015.id.isin(cohort_2011.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2011_grad_2014 = degrees_2015[degrees_2015.GRADTERM.isin([201410,201440,201470]) & degrees_2015.id.isin(cohort_2011.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2011_grad_2015 = degrees_2015[degrees_2015.GRADTERM.isin([201510,201540,201570]) & degrees_2015.id.isin(cohort_2011.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2011_grad_2016 = degrees_2016[degrees_2016.GRADTERM.isin([201610,201640,201670]) & degrees_2016.id.isin(cohort_2011.id) & ((degrees_2016.degmaj1=="CS") | (degrees_2016.degmaj1=="ACS") | (degrees_2016.degmaj2=="CS"))]
cohort_2011_grad_2017 = degrees_2017[degrees_2017.GRADTERM.isin([201710,201740,201770]) & degrees_2017.id.isin(cohort_2011.id) & ((degrees_2017.degmaj1=="CS") | (degrees_2017.degmaj1=="ACS") | (degrees_2017.degmaj2=="CS"))]

dropout_2011 = cohort_2011[(cohort_2011.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2011.id.isin(degrees_2017.id)]

'''
People who graduated from 2012 cohort
'''
cohort_2012_grad_2014 = degrees_2015[degrees_2015.GRADTERM.isin([201410,201440,201470]) & degrees_2015.id.isin(cohort_2014.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2012_grad_2015 = degrees_2015[degrees_2015.GRADTERM.isin([201510,201540,201570]) & degrees_2015.id.isin(cohort_2012.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2012_grad_2016 = degrees_2016[degrees_2016.GRADTERM.isin([201610,201640,201670]) & degrees_2016.id.isin(cohort_2012.id) & ((degrees_2016.degmaj1=="CS") | (degrees_2016.degmaj1=="ACS") | (degrees_2016.degmaj2=="CS"))]
cohort_2012_grad_2017 = degrees_2017[degrees_2017.GRADTERM.isin([201710,201740,201770]) & degrees_2017.id.isin(cohort_2012.id) & ((degrees_2017.degmaj1=="CS") | (degrees_2017.degmaj1=="ACS") | (degrees_2017.degmaj2=="CS"))]

dropout_2012 = cohort_2012[(cohort_2012.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2012.id.isin(degrees_2017.id)]

'''
People who graduated from 2013 cohort
'''
cohort_2013_grad_2015 = degrees_2015[degrees_2015.GRADTERM.isin([201510,201540,201570]) & degrees_2015.id.isin(cohort_2013.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
cohort_2013_grad_2016 = degrees_2016[degrees_2016.GRADTERM.isin([201610,201640,201670]) & degrees_2016.id.isin(cohort_2013.id) & ((degrees_2016.degmaj1=="CS") | (degrees_2016.degmaj1=="ACS") | (degrees_2016.degmaj2=="CS"))]
cohort_2013_grad_2017 = degrees_2017[degrees_2017.GRADTERM.isin([201710,201740,201770]) & degrees_2017.id.isin(cohort_2013.id) & ((degrees_2017.degmaj1=="CS") | (degrees_2017.degmaj1=="ACS") | (degrees_2017.degmaj2=="CS"))]

dropout_2013 = cohort_2013[(cohort_2013.PMAJR.isin(['CS','ACS'])==True) & ~cohort_2013.id.isin(degrees_2017.id)]

#degrees_2015[degrees_2015.id.isin(cohort_2012.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]
#cohort_2012_grad_2016 = degrees_2016[~degrees_2016.id.isin(cohort_2012_grad_2015.id) & degrees_2016.id.isin(cohort_2012.id) & ((degrees_2016.degmaj1=="CS") | (degrees_2016.degmaj1=="ACS") | (degrees_2016.degmaj2=="CS"))]
#cohort_2012_grad_2016 = cohort_2012_grad_2016.reset_index(drop=True)

#cohort_2012_grad_2017 = degrees_2017[degrees_2017.id.isin(cohort_2012.id) & (~degrees_2017.id.isin(cohort_2012_grad_2016.id)) & ((degrees_2017.degmaj1=="CS") | (degrees_2017.degmaj1=="ACS") | (degrees_2017.degmaj2=="CS"))]
#cohort_2012_grad_2017 = cohort_2012_grad_2017.reset_index(drop=True)
#cohort_2013_grad_2016 = degrees_2016[~degrees_2016.id.isin(cohort_2012_grad_2015.id) & ~degrees_2016.id.isin(cohort_2012_grad_2016.id) & degrees_2016.id.isin(cohort_2013.id) & ((degrees_2016.degmaj1=="CS") | (degrees_2016.degmaj1=="ACS") | (degrees_2016.degmaj2=="CS"))]

#cohort_2013_grad_2016 = degrees_2016[degrees_2016.id.isin(cohort_2013.id) & ((degrees_2016.degmaj1=="CS") | (degrees_2016.degmaj1=="ACS") | (degrees_2016.degmaj2=="CS"))]
#cohort_2013_grad_2016 = degrees_2016[degrees_2016.GRADTERM.isin([201610,201640,201670]) & degrees_2016.id.isin(cohort_2013.id) & ((degrees_2016.degmaj1=="CS") | (degrees_2016.degmaj1=="ACS") | (degrees_2016.degmaj2=="CS"))]

#cohort_2013_grad_2017 = degrees_2017[~degrees_2017.id.isin(cohort_2013_grad_2016.id) & degrees_2017.id.isin(cohort_2013.id) & ((degrees_2017.degmaj1=="CS") | (degrees_2017.degmaj1=="ACS") | (degrees_2017.degmaj2=="CS"))]
#print(cohort_2013_grad_2017.__len__())
#print(degrees_2015.GRADTERM==201510,201540,201570)
#cohort_2012_grad_2015 = degrees_2015[degrees_2015.GRADTERM.isin([201510,201540,201570]) & degrees_2015.id.isin(cohort_2012.id) & ((degrees_2015.degmaj1=="CS") | (degrees_2015.degmaj1=="ACS") | (degrees_2015.degmaj2=="CS"))]