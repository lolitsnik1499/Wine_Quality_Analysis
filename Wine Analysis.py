#!/usr/bin/env python
# coding: utf-8

# In[49]:


#Iporting the required liberaies
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[50]:


#loading the dataset
df = pd.read_csv("Untitled spreadsheet - winequality-red.csv")
display(df.head(10))
df.shape


# In[78]:


#Checking for Null values
df.isnull().sum()


# # let’s consider all wines with ratings 7 and above to be of very good quality, wines with 5 and 6 to be of average quality, and wines less than 5 to be of insipid quality:

# In[52]:


good_quality = df[df["quality"]>=7]
good_quality


# In[53]:


x= df.shape[0]
p_good_wine = good_quality*100/x
p_good_wine


# In[54]:


avg_quality = df[(df['quality']>=5) & (df['quality']<=6)]
avg_quality


# In[55]:


below_avg = df[df['quality']<5]
below_avg


# In[56]:


np.round(df.describe())


# In[57]:


sns.pairplot(df)


# In[79]:


plt.figure(figsize=(14, 12))
heatmap = sns.heatmap(df.corr(), annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")


# # Lets explore the co-relation in more detail
# 
# # 1.) pH and fixed acidity
# # 2.) Citric acid and fixed acidity
# # 3.) Alcohol and quality

# In[68]:


sns.scatterplot(x = df['pH'],y = df['fixed acidity'], hue = df['pH'])


# In[69]:


sns.scatterplot(x = df['citric acid'],y = df['fixed acidity'], hue = df['pH'])


# In[76]:


sns.barplot(y = df['volatile acidity'],x = df['quality'])
plt.title("Volatile acidity VS Quality")


# In[77]:


sns.barplot(y = df['alcohol'],x = df['quality'])
plt.title("Alcohol VS Quality")


# # Seems like most people generally like wines that contain a higher percentage of alcohol, ones that make them feel woozy!
# 
# # Try experimenting with more features on your own in the notebook, and see if they reveal anything. If they are related in some way, what do you think might be the reason? Exploring will reveal more hidden insights.
# 
# # It helps to remember that co-relation does not always imply causation. Sometimes when you plot graphs for two features, it might show you a pattern which might just be a co-incidence.

# In[104]:


#Outlier Detection
for feature in df.keys():
    #  Calculate Q1 (25th percentile of the data) for the given feature
    Q1 = np.percentile(df[feature], q=25)
    
    #  Calculate Q3 (75th percentile of the data) for the given feature
    Q3 = np.percentile(df[feature], q=75)
    
    #  Use the interquartile range to calculate upper and lower fence
    #Any data point below lower fence and upper fence is an outlier
    iqr = Q3 - Q1
    upper_fence = Q3 + 1.5*iqr
    lower_fence = Q1 - 1.5*iqr
    
    dfo =  df[(df[feature]<lower_fence) | (df[feature]>upper_fence)]
    
    df1 = pd.concat([dfo])
print(df1)


# In[105]:


df1


# In[109]:


#Getting all the indices of the outliers for their removal
indices = df1.index
print(indices)


# In[118]:


#Removing the outliers
good_data = df.drop(indices)
good_data

