import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


courses = pd.read_csv('C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_courses3.csv',low_memory=False)
degrees = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_degrees3.csv",low_memory=False)

x = courses["grdpts"].where(courses['DISC'] == 'MATH')
x = x.dropna()
plt.ylabel("Cumulative Math Grades for 2016")
plt.hist(x)
plt.show()
