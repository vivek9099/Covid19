#!/usr/bin/env python
# coding: utf-8

# In[19]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly
import plotly.express as px
import pandas as pd
from math import pi
df=pd.read_csv('patients_data.csv')
df.head()


# In[24]:


df.isnull().sum()


# In[25]:


df.shape


# In[8]:


df.describe()


# In[26]:


df.dropna(inplace=True)
df.head()


# In[29]:


fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.bar(df['gender'],df['age_bracket'],color='blue')
axes.set_xlabel("Age Group")
axes.set_ylabel("Total Cases")
axes.set_title("Gender Vs Total Cases")
plt.show()


# As from the above visualisation we can see the most effected age group of people from the given dataset.
# 

# In[ ]:





# In[38]:



fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(df["date_announced"],df["age_bracket"],color='blue',marker='*')
axes.set_xlabel("Date")
axes.set_ylabel("Age group")
axes.set_title("Date wise cases of effected age group ")
plt.show()
fig=px.scatter(df,x="date_announced",y="age_bracket",color='age_bracket',title='Date wise cases of effected age group')
fig.show()


# In[ ]:




