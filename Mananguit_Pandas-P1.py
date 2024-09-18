#!/usr/bin/env python
# coding: utf-8

# ## Problem 1
# #### Create a Program that loads the Cars.csv file using pandas and Display the first and last 5 rows of the data

# In[2]:


#Import pandas library to be able to use phyton data analysis
import pandas as pd 
#call the dataframe csv file named 'cars.csv' and assign it to a variable
cars = pd.read_csv('cars.csv')
#printing first five rows of the dataframe
print ('First Five Rows')
#command .head() only calls the first five rows by default
a = cars.head(5)
print (a)
#printing last five rows of the dataframe
print ('Last Five Rows')
#command .tail() only calls the last five rows by default
b = cars.tail()
print (b)



# In[ ]:




