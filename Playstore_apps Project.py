#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
from numpy import nan


# In[70]:


data=pd.read_csv(r'C:\Users\91929\OneDrive\Desktop\LINK2\playstore_apps.csv')


# In[71]:


data.head()


# In[72]:


data.info()


# In[73]:


data.describe()


# In[74]:


data.isna().sum()


# # Removing Duplicate rows

# In[75]:


data.drop_duplicates(keep='first',inplace=True)


# In[76]:


data.info()


# # Exploring for non unique values in a column to remove them

# In[77]:


print(data['Category'].unique())


# In[78]:


print(data[data['Category']=='1.9'])


# In[79]:


data.drop(data.loc[data['Category'] == "1.9"].index, inplace=True)


# In[80]:


print(data['Category'].unique())


# In[81]:


print(data['App'].unique())


# In[82]:


print(data['Rating'].unique())


# In[ ]:


# Nan values will be dealt in excel for Rating column


# In[83]:


print(data['Reviews'].unique())


# In[84]:


print(data['Size'].unique())


# In[85]:


print(data['Installs'].unique())


# In[86]:


print(data['Type'].unique())


# In[ ]:


# Nan values will be dealt in excel for Type column


# In[87]:


print(data['Price'].unique())


# In[88]:


print(data['Content Rating'].unique())


# In[89]:


print(data['Genres'].unique())


# In[90]:


print(data['Last Updated'].unique())


# In[91]:


print(data['Current Ver'].unique())


# In[92]:


print(data['Android Ver'].unique())


# In[ ]:


# Nan values will be dealt in excel for Android Ver column


# In[93]:


data.info()


# In[94]:


data.isna().sum()


# In[95]:


data.to_csv("playstore_clean.csv")


# ------------------------Cleaning Reviews data sheet----------------------------------

# In[5]:


Review_data=pd.read_csv(r'C:\Users\91929\OneDrive\Desktop\LINK2\playstore_reviews.csv')


# In[6]:


Review_data.head()


# In[7]:


Review_data.info()


# # Removing rows which has null values in Translated_Review column

# In[8]:


Review_data=Review_data.dropna()


# In[9]:


Review_data.info()


# In[10]:


Review_data.drop_duplicates(keep='first',inplace=True)


# In[11]:


Review_data.info()


# In[104]:


print(Review_data['App'].unique())


# In[105]:


print(Review_data['Translated_Review'].unique())


# In[106]:


print(Review_data['Sentiment'].unique())


# In[107]:


print(Review_data['Sentiment_Polarity'].unique())


# In[108]:


print(Review_data['Sentiment_Subjectivity'].unique())


# In[12]:


Review_data.to_csv("playstore_reviews_cleaned.csv")


# In[ ]:




