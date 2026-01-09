# filter function 
# The filter() function constructs an iterator from elements of an iterable for which a function returns true.
# syntax: filter(function, iterable)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst = list(filter(lambda x: x % 2 == 0, lst))
print(lst)  # Output: [2, 4, 6, 8,  10]


# Example 2: Using filter() to get numbers greater than 5
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  # Output: [7, 9, 11, 13, 15]

# Example 3: Using filter() to get vowels from a list of characters
chars = ['a', 'b', 'c', 'e', 'i', 'o', 'u']
vowels = list(filter(lambda x: x in 'aeiou', chars))
print(vowels)  # Output: ['a', 'e', 'i', 'o', 'u']


people = [
    {'name': 'Alice', 'age': 17},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 16},
    {'name': 'David', 'age': 22}]

def age_greater_than_18(person):
    return person['age'] > 18


list_of_adults = list(filter(age_greater_than_18, people))
print(list_of_adults)
