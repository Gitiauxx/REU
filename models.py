import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from statistics import mean
from sklearn.model_selection import cross_val_score, train_test_split

data = pd.read_csv("C:\\Users\\Pam\\Dropbox\\Data\\GradDropCS_Merged.csv")
data.drop(columns="ACT_Composite",inplace=True)
data.drop(columns="ACT_English",inplace=True)
data.drop(columns="ACT_Math",inplace=True)
data.drop(columns="ACT_Reading",inplace=True)
data.drop(columns="ACT_Science",inplace=True)
data.drop(columns="TOEFL_Convert_Paper",inplace=True)
data.drop(columns="TOEFL_Internet",inplace=True)
data.drop(columns="TOEFL_Paper",inplace=True)

data = data.fillna(0)

X = data[data.columns[:-1]]
X = pd.get_dummies(X)
y = data.iloc[:,-1]

random_forest = RandomForestClassifier(n_estimators=200)
results = cross_val_score(random_forest,X,y,cv=5,scoring='accuracy')
mean_ = mean(results)
print(mean_)