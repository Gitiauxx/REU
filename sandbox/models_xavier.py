import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split



DATA_FILE = './../data/'
features = ['cumgpa', 'term_earn_hrs', 'termgpa', 'HSGPA', 'SAT_Total_1600',
            'SAT_Verbal', 'SAT_Math']
demographic = ['ENTRY_AGE', 'SEX', 'race', 'Income']
outcome = 'dropout'

# data split
data = pd.read_csv(os.path.join(DATA_FILE, "Income_Included.csv"))

X = np.array(data[features + demographic])
y = np.array(data[outcome]).ravel()

xTrain_demo, xTest_demo, yTrain, yTest = train_test_split(X, y, test_size = 0.2, random_state = 42)
xTrain = xTrain_demo[:, :-4]
xTest = xTest_demo[:, :-4]

# train random forest
rf = RandomForestClassifier(n_estimators=200)
rf.fit(xTrain, yTrain)

# accuracy on test data
ypred_all = rf.predict(xTest)
accuracy_all = ypred_all[ypred_all  == yTest].shape[0] / ypred_all.shape[0]
print(accuracy_all)
print(yTest[yTest == 1].shape[0] / yTest.shape[0])
