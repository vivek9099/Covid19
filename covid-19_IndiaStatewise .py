#!/usr/bin/env python
# coding: utf-8

# In[35]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly
import plotly.express as px
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot

import pandas as pd
from math import pi
df=pd.read_csv('covid_19_india.csv')
df.head()


# In[7]:


df.shape


# In[8]:


df.isnull().sum()


# In[4]:


df.describe()


# In[11]:


df.groupby(['Date'])['Confirmed','Cured','Deaths','State/UnionTerritory'].max()


# In[13]:


plt.figure(figsize=(20,10))
df['State/UnionTerritory'].value_counts().plot.pie(autopct='%1.1f%%')


# In[43]:


df.plot(kind='scatter',x='Deaths',y='Confirmed')


# In[44]:


#Matplotlib
fig=plt.figure(figsize=(20,10),dpi=200)
axes=fig.add_axes([0,0,1,1])
axes.bar(df['State/UnionTerritory'],df['Confirmed'])
axes.set_title("Total Cases in India")
axes.set_xlabel("State/UnionTerritory")
axes.set_ylabel("Confirmed")
plt.show()


# In[ ]:




