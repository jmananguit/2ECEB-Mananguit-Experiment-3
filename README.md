# 2ECEB-Mananguit-Experiment-3
# Problem 1
### Creating a program that loads the Cars.csv file using pandas and Display the first and last 5 rows of the data
#### Import pandas library to be able to use phyton data analysis
``` python
import pandas as pd
```
#### Call the dataframe csv file named 'cars.csv' and assign it to a variable
``` python
cars = pd.read_csv('cars.csv')
```
#### Printing first five rows of the dataframe
#### The command .head() only calls the first five rows by default
``` python
print ('First Five Rows')
a = cars.head(5)
print (a)
```
> Output
  ```python
First Five Rows
               Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \
0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4   
1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   
2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4   
3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   
4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3   

   carb  
0     4  
1     4  
2     1  
3     1  
4     2
```
#### Printing last five rows of the dataframe
#### Command .tail() only calls the last five rows by default
``` python
print ('Last Five Rows')
b = cars.tail()
print (b)
```
> Output
  ``` python
  Last Five Rows
             Model   mpg  cyl   disp   hp  drat     wt  qsec  vs  am  gear  \
27    Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.9   1   1     5   
28  Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.5   0   1     5   
29    Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.5   0   1     5   
30   Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.6   0   1     5   
31      Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.6   1   1     4   

    carb  
27     2  
28     4  
29     6  
30     8  
31     2
```
# Problem 2
## Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
#### Import pandas library to be able to use phyton data analysis
``` python
import pandas as pd
```
#### Call the dataframe csv file named 'cars.csv' and assign it to a variable
``` python
cars = pd.read_csv('cars.csv')
```
#### Prompt user about use of the code
``` python
print('First five rows with odd-numbered columns')
```
#### Subsetting the first five rows with the syntax '[rowrange1:rowrange2:increment,colrange1:colrange2:increment]
#### Use an increment of 2 in order to skip every other column in the Dataframe 'cars'
#### Use a value of rowrange2 = 5 to limit the number of rows printed
``` python
A = cars.iloc[:5, ::2]
print (A)
```
>Output
``` python
First five rows with odd-numbered columns
               Model  cyl   hp     wt  vs  gear
0          Mazda RX4    6  110  2.620   0     4
1      Mazda RX4 Wag    6  110  2.875   0     4
2         Datsun 710    4   93  2.320   1     4
3     Hornet 4 Drive    6  110  3.215   1     3
4  Hornet Sportabout    8  175  3.440   0     3
```
### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
####prompt user about the purpose of the code 
``` python
print ('This code finds a specific car model and prints its every corresponding data')
```
#### In order the subset the correspending data of 'Mazda RX4', we can use the following code which subsets the entire row of the model
``` python
B = cars.loc[cars['Model']== 'Mazda RX4']
print (B)
```
>Output
``` python
This code finds a specific car model and prints its every corresponding data
       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb
0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4
```

### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
#### Prompt user about the purpose of the code 
``` python
print ('This code finds a specific car model and prints its number of cylinders')
```
#### Subset only the model and number of cyclinders of the selected model
``` python
print(cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']])
``` 
>Output
```python
This code finds a specific car model and prints its number of cylinders
         Model  cyl
23  Camaro Z28    8
```

### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
#### Prompt user about the purpose of the code 
``` python
print ('This code prints multiple model of cars, number of cyclinders, and highest gear of the selected model')
```
#### Subsets only the multiple model of cars, number of cyclinders, and highest gear of the selected model
#### Use boolean indexing and bitwise OR (|) operation inorder to call multiple models
``` Python
d = cars[(cars['Model'] == 'Mazda RX4 Wag') | 
     (cars['Model'] == 'Ford Pantera L') | 
     (cars['Model'] == 'Honda Civic')][['Model', 'cyl', 'gear']]
print (d)
```
>Output
``` python
This code prints multiple model of cars, number of cyclinders, and highest gear of the selected model
             Model  cyl  gear
1    Mazda RX4 Wag    6     4
18     Honda Civic    4     4
28  Ford Pantera L    8     5
```

