#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from IPython.display import display


# Misión 0

# In[ ]:


df = pd.read_csv("data.csv")
display(df.describe())


# M1

# In[ ]:


df1 = df.copy()
df1['PM2.5'].fillna(df1['PM2.5'].mean(), inplace=True)
df1['O3'].fillna(df1['O3'].mean(), inplace=True)

df2 = df.copy()
df2.dropna(subset = ["PM2.5"], inplace=True)
df2.dropna(subset = ["O3"], inplace=True)

