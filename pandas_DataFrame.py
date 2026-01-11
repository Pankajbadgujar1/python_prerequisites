# dataframe

#Create Dataframe from dictionary of list
import pandas as pd
data = {
    'Name':['pankaj','krish','jack'],
    'Age':[23,45,34],
    'City':['Bhod','Jalgaon','shirpur']

}

df = pd.DataFrame(data)
print(df)
print(type(df))

# Create array from DataFrame 
import numpy as np
print(np.array(df))

data1 = [
   
    {'Name': 'pankaj','Age':23 ,'City':'Bhod'},
    {'Name': 'krish','Age':24 ,'City':'Jalgaon'},
    {'Name': 'jack','Age':56 ,'City':'shirpur'},

]

df1 = pd.DataFrame(data1)
print(df1)
print(type(df1))

# Access single column
print(df1['Name'])

# Access The 0th row
print(df1.loc[0])
print(df.iloc[0][0])
print(df.iloc[0][1])

# Read the data files

# df2 = pd.read_csv('servay.csv')
# print(df2.head(4))  # give me first five records

# print(df2.tail(5)) # it give us last 5 records

## Accessing a specified a element

print(df1['Age'])
print(df1.at[1,'Age'])

## Accessing a specified element using iat
print(df.iat[2,2])
print(df.iat[1,2])

## Data Manipulation with DataFrame

#Adding column to df1
df1['Salary']=[500000,600,70000]
print(df1)


# Remove a column
df1.drop('Salary',axis=1,inplace=True)
print(df1)

# Add age to the column
df1['Age'] = df1['Age']+1
print(df1)