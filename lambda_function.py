# Lambda functions
# lambda functions are small anonymous functions defined using the lambda keyword.
# They can take any number of arguments but can only have one expression.

# syntax: lambda arguments: expression   
# a function without a name

def addition(x, y):
    return x + y    

add = lambda x, y: x + y
print(type(add))  # <class 'function'>
result = add(5, 3)  # 8
print(result)

# Example 1: A lambda function that squares a number
square = lambda x: x * x
print(square(4))  # Output: 16 

# Example 2: A lambda function that adds two numbers
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Example 3: A lambda function used with the map() function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 4: A lambda function used with the filter() function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Example 5: A lambda function used with the sorted() function
points = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_points = sorted(points, key=lambda point: point[1])  
print(sorted_points)  # Output: [(3, 1), (1, 2), (2, 3), (5, 4)]

# Example 6: A lambda function used with reduce() function
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1*2*3*4*5=120)
