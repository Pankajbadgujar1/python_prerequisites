"""
Pandas : 
Pandas is a powerful data mainipulation library in Python , widely used for data analysis and data cleaning.
It provides two primary data structures : Series and DataFrame.

Series : A Series is one -dimentional array like object that can hold any data type .
         It is similar to column in a table 

DataFrame : Dataframe is two-dimentional , size-mutable, and potentially heterogeneous tabular
            data structure with labeled axes(rows and columns)

"""
import pandas as pd

## series 

data =[1,2,3,4,5]
series = pd.Series(data)
print(series)
print(type(series))

## Create  a Series from dictionary
data1 = {'a':1,'b':2,'c':4}
series_dict = pd.Series(data1)
print(series_dict)

## give difference index
data2 = [10,20,30,40]
index = ['a','b','c','d']

se = pd.Series(data2,index=index) 

print(se)


