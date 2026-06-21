## loading csv dataset to pandas Dataframe
import pandas as pd
from sklearn import model_selection
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

dt = pd.read_csv('F:\\Coding\\Projects\\hdp2\\HDP_Data.csv')

## renaming features to proper name
dt.columns = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholesterol', 'fasting_blood_sugar', 'rest_ecg', 'max_heart_rate_achieved',
       'exercise_induced_angina', 'st_depression', 'st_slope','target']

## checking for missing values
dt.isnull().sum()

##Splitting the Features and Target.

X = dt.drop(columns='target')
Y = dt['target']

##Splitting the Data into Training data & Test Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

##Model Training
##Declearing the RandomForestClassification model:

rfmodel= RandomForestClassifier(max_depth = 10,criterion="entropy")

##Training the RFC Model:

# now we are training the machine learning models with Training data 
rfmodel.fit(X_train, Y_train)

#10-fold cross-validation 
#cv = KFold(n_splits=10, random_state=1, shuffle=True)
kfold = model_selection.KFold(n_splits=20)
result3 = model_selection.cross_val_score(rfmodel, X_train, Y_train, cv=kfold)

# Save the trained model as a pickle string.

saved_RFmodel = pickle.dumps(rfmodel)

filename = 'RFmodel88_test02.sav'
pickle.dump(rfmodel, open(filename, 'wb'))
