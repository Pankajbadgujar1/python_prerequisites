import pandas as pd

# read data from csv
df = pd.read_csv("sampledata.csv")
print(df.head())

# read from exel file
df = pd.read_excel("sales_data.xlsx")
print(df.head())


#From JSON string
data = [
    {"name": "James", "age": 25},
    {"name": "Anna", "age": 30}
]
df = pd.DataFrame(data)
print(df)


# Read Data from Database (SQL)
# import sqlite3

# conn = sqlite3.connect("example.db")
# df = pd.read_sql("SELECT * FROM users", conn)
# print(df)


