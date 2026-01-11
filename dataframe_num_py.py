import pandas as pd

df = pd.read_csv('sampledata.csv')
print(df)

print(df.describe())

print(df.dtypes)

# Handling missing values
print([df.isnull()])

print([df.isnull().any()])

sum = df.isnull().sum()
print(sum)

# Fill missing values

df_filled = df.fillna(0)
print(df.dtypes)

# Rename the table name
df = df.rename(columns={'date':'sales Date'})
print(df)

# Change datatypes
df['value_new'] = df['value'].astype(int)
print(df)