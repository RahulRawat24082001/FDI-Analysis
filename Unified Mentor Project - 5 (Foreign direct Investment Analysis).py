#!/usr/bin/env python
# coding: utf-8

# # Foreign Direct Investment Analysis

# ### Importing Important Python Libraries 

# In[1]:


import pandas as pd 
import numpy as np


# ### Importing Data or Reading Data :- 

# In[39]:


df = pd.read_csv("C:/Users/rawat/Downloads/FDI data.csv",index_col=0)


# In[38]:


df.head()


# **Checking the Data types of all the columns for an easy data cleaning/Wrangling :**

# In[29]:


df["2000-01"]


# In[4]:


df.dtypes


# ## Calculating the total FDI in each sector : 

# In[5]:


df['total_fdi'] = df.iloc[:, 1:].sum(axis=1)


# In[6]:


df


# **Checking wether their is any Null values or NAN (Not an integer value) :-**

# In[7]:


df.isna()


# ### After all of this we will find mean and median of all the years in all Sectors :- 

# In[8]:


df['mean_fdi'] = df.iloc[:, 1:].mean(axis=1)
df['median_fdi'] = df.iloc[:, 1:].median(axis=1)


# In[9]:


df


# ### Transposing data for finding the correlation between Different-Different sectors :- 

# In[40]:


# Using numpy.transpose
transposed_data_1 = np.transpose(df)
print(transposed_data_1)


# In[43]:


transposed_data_1


# In[42]:


transposed_data_1.index.name = "Years"


# ###  Calculate the correlation between FDI and year :- 

# In[44]:


corr_matrix = transposed_data_1.corr()
corr_matrix


# ### After all of the data cleaning and finding out the correlation, I am going to save these to files for further step (visualization) .

# In[45]:


transposed_data_1.to_csv("Transposed data FDI.csv")


# In[37]:


df.to_csv("Modified FDI data.csv")


# ### So after finding correlation we got to know the key factors effecting and correlations between different sectors which are effecting other sectors. 

# ###  After all of these steps, Next step for the Foreign direct investment Analysis is Data Visualization. For data visualization in python I prefer Seaborn and matplotlib libraries for the visualization or for other sources I prefer Power BI for visualization but according to your Terms and conditions I am going to use tableau and Further analysis has been done in the tableau attached with this file. 

# # Data Cleaning and Wrangling done !!  :)

# In[1]:


pip install nbconvert


# In[4]:





# In[ ]:




