import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import KBinsDiscretizer
from keras.wrappers.scikit_learn import KerasClassifier
from scipy import stats
from sklearn.model_selection import StratifiedKFold
import numpy

data = pd.read_csv("/Users/abhi/Documents/abhi_data/STEM_Grad_6_Years_new.csv")
data.drop(columns=["Application_Major",'cohort','TERMBNR','cohort_pcoll','cohort_pmajr','Permanent_Address_ZIP','PMAJR','Permanent_Address_STATE','PCOLL',"Application_College"],inplace=True)

def create_baseline():
	# create model
	model = Sequential()
	model.add(Dense(20, input_dim=20, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
	# Compile model
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


X = data[data.columns[:-1]]
X.drop(columns=["id"],inplace=True)

X = pd.get_dummies(X)
esc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
X = esc.fit_transform(X)
y = data.iloc[:,-1]



seed = 7
numpy.random.seed(seed)
scoring = 'f1_macro'
# define 10-fold cross validation test harness
estimator = KerasClassifier(build_fn=create_baseline, epochs=100, batch_size=5, verbose=0)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, y, cv=kfold,scoring=scoring)
print("Results: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))