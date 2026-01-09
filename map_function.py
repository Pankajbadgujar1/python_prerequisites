# The map function 
# The map() function applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).
# syntax: map(function, iterable)

# Example 1: Using map() with a regular function
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 2: Using map() with a lambda function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 3: Using map() to convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]   
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print(fahrenheit)  # Output: [32.0, 50.0,

# 68.0, 86.0, 104.0]

# example 4 : list to string conversion
numbers = [1, 2, 3, 4, 5]
string_numbers = list(map(str, numbers))
print(string_numbers)  # Output: ['1', '2', '3', '4', '5']

#conclusion : The map() function is a powerful tool for applying functions to iterables
#  in a concise manner, especially when combined with lambda functions for simple operations.