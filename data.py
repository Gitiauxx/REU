import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle


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

if __name__ == '__main__':
    #courses = pd.read_csv('C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_courses3.csv', low_memory=False)
    #degrees = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\nsf_ftf_degrees3.csv", low_memory=False)

    # demographics_16_15 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2016\\2016_2015_demographics.csv",low_memory=False)

    pickle_in = open("C:\\Users\\Pam\\Documents\\REU\\course.pickle", "rb")
    courses = pickle.load(pickle_in)

    pickle_in_2 = open("C:\\Users\\Pam\\Documents\\REU\\degree.pickle","rb")
    degrees = pickle.load(pickle_in_2)

    sample = degrees[(degrees['degmaj1'].isin(['CS']) == True) | (degrees['degmaj1'].isin(['ACS']) == True)]
    # use isin==True to get all CS and ACS degrees
    sample = sample.dropna(axis=1, how='all')
    # drop columns with ALL NA's

    # sample = sample.fillna("None")
    # fill NA's with None (no major)
    sample = sample.reset_index(drop=True)
    # reset the indicies of the whole dataframe for easier analysis
    sample['id'] = sample['id'].astype(int)
    # cast the id values as int (Python automatically casts them as float for some reason)

    sample = sample.fillna(0).to_sparse(fill_value=0)
    # make into sparse matrix, filling in NA's with 0's

    '''
    x = courses["grdpts"].where(courses['DISC'] == 'MATH')
    x = x.dropna()
    plt.ylabel("Cumulative Math Grades for 2016")
    plt.hist(x)
    plt.show()
    #histogram
    '''