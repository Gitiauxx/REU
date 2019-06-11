import pandas as pd

# dropout: students that show up in the students files in 2015 but not in the students file / degree file in 2016
student2015 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2015\\nsf_ftf_student2.csv", low_memory=False)
student2015.drop_duplicates('id', inplace=True)

student2016 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_student3.csv", low_memory=False)
student2016.drop_duplicates('id', inplace=True)

student2017 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2017\\nsf_ftf_student4.csv", low_memory=False)
student2017.drop_duplicates('id', inplace=True)

dropout = student2015[(~student2015.id.isin(student2016.id)) & (~student2015.id.isin(student2017.id)) & ((student2015.PMAJR.isin(['CS'])==True) | (student2015.PMAJR.isin(['ACS'])==True))]
#statement checks for: 2015 student ID's that are NOT in 2016/2017 & CS/ACS
dropout = dropout.reset_index(drop=True)
print(dropout)