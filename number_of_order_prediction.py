# -*- coding: utf-8 -*-
"""Number_of_order_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z6jFw-Ungh4Gc19_Akmqucp224FgseYo
"""

import pandas as pd
import numpy as np

dataset=pd.read_csv('/content/TRAIN.csv')
dataset

dataset.info()

dataset.isnull().sum()

dataset.describe()

import plotly.express as px

pie=dataset["Store_Type"].value_counts()
store=pie.index
orders=pie.values
fig=px.pie(dataset,values=orders,names=store)
fig.show()

pie2=dataset["Location_Type"].value_counts()
location=pie2.index
orders=pie2.values
fig=px.pie(dataset,values=orders,names=location)
fig.show()

pie3=dataset["Region_Code"].value_counts()
code=pie3.index
orders=pie3.values
fig=px.pie(dataset,values=orders,names=code)
fig.show()

pie4=dataset["Discount"].value_counts()
discount=pie4.index
orders=pie4.values
fig=px.pie(dataset,values=orders,names=discount)
fig.show()

pie5=dataset["Holiday"].value_counts()
holiday=pie5.index
orders=pie5.values
fig=px.pie(dataset,values=orders,names=holiday)
fig.show()

dataset["Discount"]=dataset["Discount"].map({"Yes":1,"No":0})
dataset

dataset["Store_Type"]=dataset["Store_Type"].map({"S1":1,"S2":2,"S3":3,"S4":4})
dataset

dataset["Location_Type"]=dataset["Location_Type"].map({"L1":1,"L2":2,"L3":3,"L4":4,"L5":5})
dataset

X=np.array(dataset[["Store_Type","Location_Type","Holiday","Discount"]])
Y=np.array(dataset['#Order'])

X

Y

#Making the model
from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2,random_state=42)

#using gradient boost regression
import lightgbm as ltb
model=ltb.LGBMRegressor()

model.fit(X_train,Y_train)

Y_predic=model.predict(X_test)

Y_predic

Y_test

data_predic=pd.DataFrame(data={"Predicted Orders": Y_predic.flatten()})

data_predic

