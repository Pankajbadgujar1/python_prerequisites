e object that can hold any data type .
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
