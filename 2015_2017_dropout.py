import pandas as pd

if __name__ == '__main__':
    degrees_2015 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2015\\nsf_ftf_degrees2.csv", low_memory=False)
    degrees_2015 = degrees_2015[
        (degrees_2015['degmaj1'].isin(['CS']) == True) | (degrees_2015['degmaj1'].isin(['ACS']) == True)]
    # load degrees in 2015 that are only CS and ACS

    degrees_2017 = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\FTF\\Fall2017\\nsf_ftf_degrees4.csv", low_memory=False)
    degrees_2017 = degrees_2017[
        (degrees_2017['degmaj1'].isin(['CS']) == True) | (degrees_2017['degmaj1'].isin(['ACS']) == True)]
    # load degrees in 2017 that are only CS and ACS

    degrees_2015 = degrees_2015.reset_index(drop=True)
    degrees_2017 = degrees_2017.reset_index(drop=True)
    # reset indicies for easier viewing

    degree_drop = degrees_2015[degrees_2015["cohort"].isin(degrees_2017["cohort"])]
    # check which ID's are the same
    degree_drop = degree_drop.reset_index(drop=True)

    # from here, you can either debug in Pycharm or print the dataframes to see the differences
    print(degree_drop)