#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys #tuve que usar esto para poder importar sklearn, pandas y numpy
get_ipython().system('{sys.executable} -m pip install sklearn')
get_ipython().system('{sys.executable} -m pip install pandas')
get_ipython().system('{sys.executable} -m pip install numpy')


# In[2]:


import pandas as pd
import numpy as np
import sklearn as sk
from IPython.core.display import display
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data.csv")
display(df.head())
pd.isna(df).value_counts()
#elimino las entradas con más de un NaN
df = df.dropna(thresh=6)
pd.isna(df).value_counts()

vars = ['Year','Month','Day']
label_encoder = LabelEncoder()
for i in vars:
    df[i] = label_encoder.fit_transform(df[i])
df.dtypes

training_set, test_set = train_test_split(vars.copy(), test_size = 0.3)
training_set, validation_set = train_test_split(training_set.copy(), test_size = 0.1)

print(f'Tamaño set entrenamiento: {len(training_set)}')
print(f'Tamaño set validación: {len(validation_set)}')
print(f'Tamaño set test: {len(test_set)}')

#data = pd.read_csv(f'data.csv').rename(columns={'Unnamed: 0': 'Index'}).set_index('Index')
#data.head()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = ['O3','PM2.5','Environmental_risk']

#training_set[features] = scaler.fit_transform(training_set[features])
#validation_set[features] = scaler.transform(validation_set[features])
#test_set[features] = scaler.transform(test_set[features])

#training_set.head()


# In[ ]:




