# The map function 
# The map() function applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).
# syntax: map(function, iterable)

# Example 1: Using map() with a regular function
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))