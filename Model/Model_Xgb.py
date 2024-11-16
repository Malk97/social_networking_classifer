import numpy as np
import pandas as pd 
import joblib
from sklearn import preprocessing, model_selection
import xgboost as xgb

data = pd.read_csv('Data/Social_Network_Ads.csv')

data.drop_duplicates(inplace=True)
data.drop(columns = ['User ID'], inplace = True)

data['Gender'] = data['Gender'].replace({'Male': 1, 'Female':0})

x = data.drop(columns= ['Purchased'])
y = data.Purchased

x_normalize = preprocessing.StandardScaler()
x_norm = x_normalize.fit_transform(x)


x_train, x_test, y_train, y_test = model_selection.train_test_split(x_norm, y, test_size= 0.1, random_state=42)


xgb_model = xgb.XGBClassifier()
xgb_model.fit(x_train, y_train)

joblib.dump(xgb_model,'xgb_model.json')
