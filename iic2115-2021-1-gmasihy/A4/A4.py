#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sklearn as sk
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys #tuve que usar esto para poder importar seaborn
get_ipython().system('{sys.executable} -m pip install seaborn')
import seaborn as sns
from sklearn import metrics, ensemble, decomposition
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from IPython.display import display
get_ipython().run_line_magic('matplotlib', 'inline')
np.random.seed(742390)


# Preparación y M1

# In[2]:


df = pd.read_csv("data.csv")
print(f"N° de datos: {len(df)}")
display(df.head())
display(df.describe())


# In[3]:


df = df.dropna(thresh=6)
pd.isna(df).value_counts()


# In[4]:


label_encoder = LabelEncoder()
for i in ["DayOfWeek", "SchoolHoliday","Date"]:
    df[i] = label_encoder.fit_transform(df[i])
df["Store"] = label_encoder.fit_transform(df["Store"].astype(str))
df["Sales"] = label_encoder.fit_transform(df["Sales"].astype(str))
df["Customers"] = label_encoder.fit_transform(df["Customers"].astype(str))
df["Open"] = label_encoder.fit_transform(df["Open"].astype(str))
df["Promo"] = label_encoder.fit_transform(df["Promo"].astype(str))
df.head()


# Como se puede observar, tanto para DayOfWeek como para StateHoliday hay algunos datos faltantes. 3 y 2, respectivamente.

# In[5]:


cond1 = ~(df["Store"].isna() | df["DayOfWeek"].isna() | df["Date"].isna() | df["Sales"].isna() | df["Customers"]| df["Open"]| df["Promo"]| df["StateHoliday"]| df["SchoolHoliday"].isna())
df_pred = df[cond1].copy()
training_set, test_set = train_test_split(df_pred.copy(), test_size = 0.3)

print(f'Tamaño set entrenamiento: {len(training_set)}')
print(f'Tamaño set test: {len(test_set)}')


# In[6]:


scaler = StandardScaler()
var_num = ["Sales"]

training_set[var_num] = scaler.fit_transform(training_set[var_num])
test_set[var_num] = scaler.transform(test_set[var_num])

training_set.head()


# In[7]:


#features = ["Store", "DayOfWeek", "Date", "Sales","Customers","Open","Promo","StateHoliday","SchoolHoliday"]
#target = "Sales"
#reg1 = LinearRegression()
#reg1.fit(training_set[features], training_set[target])
#predictions = reg1.predict(test_set[features])
#mse = metrics.mean_squared_error(test_set[target], predictions)
#print(f"Error cuadrático medio: {mse}")


# In[9]:


df = df.dropna(thresh=6)
pd.isna(df).value_counts()


# In[10]:


values1 = set(df['DayOfWeek']).difference(set(['.', np.nan]))
dow_translator = {}
for i, k in enumerate(values1):
    dow_translator[k] = i+1
    dow_translator[i+1] = i+1


# In[11]:


values2 = set(df['Date']).difference(set(['.', np.nan]))
date_translator = {}
for i, k in enumerate(values2):
    date_translator[k] = i+1
    date_translator[i+1] = i+1


# In[12]:


values3 = set(df['Sales']).difference(set(['.', np.nan]))
sales_translator = {}
for i, k in enumerate(values3):
    sales_translator[k] = i+1
    sales_translator[i+1] = i+1


# In[13]:


values4 = set(df['Customers']).difference(set(['.', np.nan]))
customers_translator = {}
for i, k in enumerate(values4):
    customers_translator[k] = i+1
    customers_translator[i+1] = i+1


# In[14]:


values5 = set(df['Open']).difference(set(['.', np.nan]))
open_translator = {}
for i, k in enumerate(values5):
    open_translator[k] = i+1
    open_translator[i+1] = i+1


# In[15]:


values6 = set(df['Promo']).difference(set(['.', np.nan]))
promo_translator = {}
for i, k in enumerate(values6):
    promo_translator[k] = i+1
    promo_translator[i+1] = i+1


# In[16]:


values7 = set(df['StateHoliday']).difference(set(['.', np.nan]))
stateholiday_translator = {}
for i, k in enumerate(values7):
    stateholiday_translator[k] = i+1
    stateholiday_translator[i+1] = i+1


# In[17]:


values8 = set(df['SchoolHoliday']).difference(set(['.', np.nan]))
schoolholiday_translator = {}
for i, k in enumerate(values8):
    schoolholiday_translator[k] = i+1
    schoolholiday_translator[i+1] = i+1


# In[18]:


dow_translator[np.nan] = np.nan
dow_translator['.'] = np.nan

date_translator[np.nan] = np.nan
date_translator['.'] = np.nan

sales_translator[np.nan] = np.nan
sales_translator['.'] = np.nan

customers_translator[np.nan] = np.nan
customers_translator['.'] = np.nan

open_translator[np.nan] = np.nan
open_translator['.'] = np.nan

promo_translator[np.nan] = np.nan
promo_translator['.'] = np.nan

stateholiday_translator[np.nan] = np.nan
stateholiday_translator['.'] = np.nan

schoolholiday_translator[np.nan] = np.nan
schoolholiday_translator['.'] = np.nan


# In[19]:


df['Sales'] = df['Sales'].apply(lambda x: sales_translator[x])
pd.isna(df).value_counts()

