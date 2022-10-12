import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset_name = str(input("Enter the Dataset Name: "))

dataset = pd.read_csv(dataset_name)
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
y = y.reshape(len(y),1)

# Splitting into training and test dataset

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.svm import SVC
model = SVC(kernel='rbf',random_state=0)
model.fit(X_train,y_train.ravel())
print("The model is ready to predict")

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))
