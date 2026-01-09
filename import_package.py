from math import sqrt, pi

print(f"The square root of 16 is {sqrt(16)}")
print(f"The value of pi is approximately {pi}")

def calculate_circle_area(radius):
    return pi * radius * radius

radius = 5
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area}")


# array example
import array as arr
# creating an array of integers
numbers = arr.array('i', [1, 2, 3, 4, 5])
print("Array elements:")
for num in numbers:
    print(num)  


import random
# generating a random integer between 1 and 100
random_integer = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_integer}")    


import os
# getting the current working directory
current_directory = os.getcwd()
#create a new directory
new_directory = os.path.join(current_directory, 'new_folder')
os.makedirs(new_directory, exist_ok=True)
print(f"Current Directory: {current_directory}")


# use json
import json
#convert dict into json 
data= {'name':'krish','age':25}
json_str =json.dumps(data)
print(json_str)
print(type(json_str))

# convert json data into dict
parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data))

# use csv

import csv
with open('sample.txt',mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['Pankaj',32])


# Use Of datetime 

from datetime import datetime,timedelta

now=datetime.now()
print(now)

yesterday = now-timedelta(days=1)
print(yesterday)


# Use regular expression

import re
pattern='\d+'
text = 'There are 123 apples 456'
match=re.search(pattern,text)
print(match.group())
