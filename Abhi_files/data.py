import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import pickle

# courses = pd.read_csv('C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_courses3.csv', low_memory=False)
# degrees = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_degrees3.csv", low_memory=False)
# demographics_16_15 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\2016_2015_demographics.csv",low_memory=False)

if __name__ == '__main__':
    pickle_in = open("C:\\Users\\Pam\\Documents\\REU\\course.pickle", "rb")
    courses = pickle.load(pickle_in)

    pickle_in_2 = open("C:\\Users\\Pam\\Documents\\REU\\degree.pickle","rb")
    degrees = pickle.load(pickle_in_2)


    degrees_2015 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2015\\nsf_ftf_degrees2.csv", low_memory=False)
    degrees_2015 = degrees_2015[(degrees_2015['degmaj1'].isin(['CS']) == True) | (degrees_2015['degmaj1'].isin(['ACS']) == True)]
    #load degrees in 2015 that are only CS and ACS

    degrees_2017 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2017\\nsf_ftf_degrees4.csv", low_memory=False)
    degrees_2017 = degrees_2017[(degrees_2017['degmaj1'].isin(['CS']) == True) | (degrees_2017['degmaj1'].isin(['ACS']) == True)]
    # load degrees in 2017 that are only CS and ACS

    degrees_2015 = degrees_2015.reset_index(drop=True)
    degrees_2017 = degrees_2017.reset_index(drop=True)
    #reset indicies for easier viewing

    degree_drop = degrees_2015[degrees_2015["cohort"].isin(degrees_2017["cohort"])]
    #check which ID's are the same
    degree_drop = degree_drop.reset_index(drop=True)
    print(degree_drop)
    exit(2)

    '''
    sample = degrees[(degrees['degmaj1'].isin(['CS']) == True) | (degrees['degmaj1'].isin(['ACS']) == True)]
    # use isin==True to get all CS and ACS degrees
    sample = sample.dropna(axis=1, how='all')
    # drop columns with ALL NA's

    # sample = sample.fillna("None")
    # fill NA's with None (no major)
    sample = sample.reset_index(drop=True)
    # reset the indicies of the whole dataframe for easier analysis

    degrees_2017 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2017\\nsf_ftf_degrees4.csv", low_memory=False)
#    degree_sample = degrees_2017[degrees_2017["id"].isin(sample["id"])] #degrees_2017[degrees_2017["id"].isin(degrees)]
    sample_2 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2017\\nsf_ftf_degrees4.csv", low_memory=False)
#    degree_sample = sample[sample["id"].isin(degrees_2017["id"])]
#    degree_sample = degree_sample.reset_index(drop=True)
    degrees_2017 = degrees[(degrees['degmaj1'].isin(['CS']) == True) | (degrees['degmaj1'].isin(['ACS']) == True)]
    degree_drop = degrees_2017[degrees_2017["id"].isin(degrees["id"])] #degrees_2017[degrees_2017["id"].isin(degrees)]
    print("helo")
    exit(2)
    
    sample['id'] = sample['id'].astype(int)
    # cast the id values as int (Python automatically casts them as float for some reason)

    sample = sample.fillna(0).to_sparse(fill_value=0)
    # make into sparse matrix, filling in NA's with 0's
    print("hello")
#    y = data.iloc[:, -1]
#    xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=0)

#    regressor = RandomForestRegressor(n_estimators=20,random_state=0)
#    results = cross_val_score(neigh, X, y, cv=5, scoring='f1_weighted')
'''
def storeData():
    courses = pd.read_csv('C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_courses3.csv', low_memory=False)
    course_pickle = open("C:\\Users\\Pam\\Documents\\REU\\course.pickle","wb")
    pickle.dump(courses,course_pickle)
    course_pickle.close()

    degrees = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_degrees3.csv", low_memory=False)
    degree_pickle = open("C:\\Users\\Pam\\Documents\\REU\\degree.pickle","wb")
    pickle.dump(degrees,degree_pickle)
    degree_pickle.close()

#storeData()
#method only called once to pickle datasets
'''
x = courses["grdpts"].where(courses['DISC'] == 'MATH')
x = x.dropna()
plt.ylabel("Cumulative Math Grades for 2016")
plt.hist(x)
plt.show()
#histogram
'''