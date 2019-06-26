import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from scipy.stats import shapiro
from scipy import stats
from sklearn.linear_model import LogisticRegression
#from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import cross_val_score, train_test_split

data = pd.read_csv("/Users/abhi/Documents/REU/Final_Merged.csv")

zipcode_income = pd.read_csv('/Users/abhi/Documents/MedianZIP-3.csv')

data.rename(columns={'Permanent_Address_ZIP': 'Zip'}, inplace=True)
data['Zip'] = data.Zip.apply(lambda x: int(str(x)[:5]))

new_data = data.merge(zipcode_income,on="Zip")
cols = list(new_data.columns.values)

new_data=new_data[['id', 'cohort', 'cohort_pcoll', 'cohort_pmajr', 'PCOLL', 'PMAJR', 'TERMBNR', 'cumgpa', 'term_earn_hrs', 'termgpa', 'ENTRY_AGE', 'SEX', 'race', 'Permanent_Address_STATE', 'Median', 'Application_College', 'Application_Major', 'HSGPA', 'SAT_Total_1600', 'SAT_Verbal', 'SAT_Math', 'dropout']
]
#removed zip and replaced with median income according to zip

new_data['Median'] = new_data['Median'].str.replace(',', '')
new_data.rename(columns={'Median': 'Income'}, inplace=True)
new_data['Income'] = new_data['Income'].astype(int)

data=new_data.copy(deep=True)
data.drop(columns=['cohort_pcoll','cohort_pmajr','Income','PMAJR','TERMBNR','cohort','Permanent_Address_STATE','PCOLL',"Application_College"],inplace=True)


'''
new_data.hist(column="Income")

x = new_data.hist(column="Income")
#plt.show(x)

np.random.seed(12345678)

income = pd.DataFrame(new_data["Income"])

income = preprocessing.normalize(income)

stat, p = shapiro(income)
print(stat, p)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')

exit(2)
'''


X = data[data.columns[:-1]]
X.drop(columns="id",inplace=True)
X = pd.get_dummies(X)
y = data.iloc[:,-1]


random_forest = RandomForestClassifier(n_estimators=1000)
#logisticCV = linear_model.LogisticRegressionCV(cv=30,max_iter=6000000)
#decision_tree = svm.SVC(gamma="scale",kernel='rbf',C=.0000001)
#ada_boost = AdaBoostClassifier()
#neural_network = MLPClassifier(max_iter=10000)

xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size = 0.2, random_state = 42)
neigh = random_forest.fit(xTrain,yTrain)
forest = RandomForestClassifier(n_estimators=1000)


forest.fit(X,y)
feature_importances = pd.DataFrame(forest.feature_importances_,
                                   index = xTrain.columns,
                                    columns=['importance']).sort_values('importance',                                                                 ascending=False)
print(feature_importances.head(10))
#exit(2)


predict = neigh.predict(xTest)
accuracy = accuracy_score(yTest,predict)
print("\n")
print("accuracy: ")
print(accuracy)

#f1 = f1_score(yTest,predict,average='weighted')
#results = cross_val_score(logisticCV,X,y,cv=5,scoring='f1_weighted')
#mean_ = mean(results)
#print(mean_)
'''
logisticCV.fit(X,y)
print(logisticCV.coef_)
exit(2)
'''
#data.to_csv(r"/Users/abhi/Documents/REU/Income_Included.csv")
#dropout_income = data[data.dropout==0]
#print(dropout_income["Income"].mean())
#print("\n")

#exit(2)

'''
data = data[data.cohort != 201010]
data = data[data.cohort != 201070]
data = data[data.TERMBNR != 201010]
data = data[data.TERMBNR != 201070]
'''
#drop 2010


#data = data[data.cohort != 201370]
#data = data[data.TERMBNR != 201370]
#drop 2013

#data.drop(columns="2013",inplace=True)
#data.drop(columns="cohort",inplace=True)
#data.drop(columns="TERMBNR",inplace=True)

'''
data = data.dropna(how='any')
data = data.reset_index(drop=True)

data_2009 = data[(data.cohort.isin(['200970'])==True) | (data.cohort.isin(['200910'])==True) | (data.cohort.isin(['200940'])==True)]
ratio_2009 = data_2009['dropout'].value_counts().to_frame().reset_index().rename(columns={'index':'values', 'values':'count'})

data_2010 = data[(data.cohort.isin(['201070'])==True) | (data.cohort.isin(['201010'])==True) | (data.cohort.isin(['201040'])==True)]
data_2010 = data_2010.reset_index(drop=True)
ratio_2010 = data_2010['dropout'].value_counts().to_frame().reset_index().rename(columns={'index':'values', 'values':'count'})

data_2011 = data[(data.cohort.isin(['201170'])==True) | (data.cohort.isin(['201110'])==True) | (data.cohort.isin(['201140'])==True)]
data_2011 = data_2011.reset_index(drop=True)
ratio_2011 = data_2011['dropout'].value_counts().to_frame().reset_index().rename(columns={'index':'values', 'values':'count'})

data_2012 = data[(data.cohort.isin(['201270'])==True) | (data.cohort.isin(['201210'])==True) | (data.cohort.isin(['201240'])==True)]
data_2012 = data_2012.reset_index(drop=True)
ratio_2012 = data_2012['dropout'].value_counts().to_frame().reset_index().rename(columns={'index':'values', 'values':'count'})

data_2013 = data[(data.cohort.isin(['201370'])==True) | (data.cohort.isin(['201310'])==True) | (data.cohort.isin(['201340'])==True)]
data_2013 = data_2013.reset_index(drop=True)
ratio_2013 = data_2013['dropout'].value_counts().to_frame().reset_index().rename(columns={'index':'values', 'values':'count'})
'''

#data = data.fillna(0)
#data_null = data.loc[:, data.isna().any()]
#data_null.to_csv(r"C:\\Users\\Pam\\Documents\\REU\\null_data.csv")
#exit(2)

'''
data = pd.get_dummies(data)
data.to_csv(r"C:\\Users\\Pam\\Documents\\REU\\new_data.csv")
exit(2)
'''