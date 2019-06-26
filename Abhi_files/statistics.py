import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from Cython.Shadow import inline


#students_total = pd.read_csv("/Users/abhi/Dropbox/Data/TTF/Fall2017/nsf_ftf_student4.csv", usecols=['id', 'cohort', 'cohort_pmajr','cumgpa2'])

nova_students_total = pd.read_csv("/Users/abhi/Dropbox/Data/TR/Fall2017/nsf_tr_student4.csv", usecols=['id', 'cohort', 'cohort_pmajr','cumgpa'])

nova_students_total.drop_duplicates('id',inplace=True)
nova_students_total = nova_students_total[(nova_students_total.cohort_pmajr.isin(['CS','ACS','GAME'])==True)]

student_data = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_student4.csv",usecols=['id', 'cohort','cumgpa2'])

#admissions_total = pd.read_csv("/Users/abhi/Dropbox/Data/FTF/Fall2017/nsf_ftf_admissions4.csv", usecols=['id','HSGPA','SAT_Total_1600'])
#admissions_total.drop_duplicates('id',inplace=True)

merge_students_admissions = students_total.merge(admissions_total,on='id')
merge_students_admissions = merge_students_admissions.replace('.', np.nan)
merge_students_admissions = merge_students_admissions.dropna(how='any')
merge_students_admissions = merge_students_admissions.reset_index(drop=True)
merge_students_admissions.drop(columns="id",inplace=True)

merge_students_admissions.cumgpa2 = merge_students_admissions.cumgpa2.astype(float)


import seaborn as sns
corr = merge_students_admissions.corr()
# plot the heatmap
sns.heatmap(corr,
        xticklabels=corr.columns,
        yticklabels=corr.columns,annot=True)
plt.show()

print("hr")