#!/usr/bin/env python
# coding: utf-8

# ## Problem 2
# ## Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
# #### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
# 

# In[2]:


#Import pandas library to be able to use phyton data analysis
import pandas as pd
#call the dataframe csv file named 'cars.csv' and assign it to a variable
cars = pd.read_csv('cars.csv')

#Part A
#Prompt user about use of the code
print('First five rows with odd-numbered columns')
#Subsetting the first five rows with the syntax '[rowrange1:rowrange2:increment,colrange1:colrange2:increment]
#Use an increment of 2 inorder to skip every other column in the Dataframe
# use a value of rowrange2 = 5 to limit the number of rows printed
A = cars.iloc[:5, ::2]
print (A)


# #### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[4]:


#part b
#prompt user about the purpose of the code 
print ('This code finds a specific car model and prints its every corresponding data')
#In order the subset the correspending data of 'Mazda RX4', we can use the following code which subsets the entire row of the model
B = cars.loc[cars['Model']== 'Mazda RX4']
print (B)


# #### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[6]:


#part c
#prompt user about the purpose of the code 
print ('This code finds a specific car model and prints its number of cylinders')
#Subsets only the model and number of cyclinders of the selected model
print(cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']])


# #### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[8]:


#part d
#prompt user about the purpose of the code 
#Subsets only the multiple model of cars, number of cyclinders, and highest gear of the selected model
print ('This code prints multiple model of cars, number of cyclinders, and highest gear of the selected model')
#Use boolean indexing and bitwise OR (|) operation inorder to call multiple models
d = cars[(cars['Model'] == 'Mazda RX4 Wag') | 
     (cars['Model'] == 'Ford Pantera L') | 
     (cars['Model'] == 'Honda Civic')][['Model', 'cyl', 'gear']]
print (d)

