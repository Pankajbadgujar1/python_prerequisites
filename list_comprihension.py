lst = []
for i in range(10):
    lst.append(i**2)

print(lst)

#Comprihension version of above code 
print([i**2 for i in range(10)])

# Basics Syntax [expression for item in iterble]

# with control logic [expression for item in iterable if condition]

## Basic list Comprihension

square = [num**2 for num in range(10)] 
print(square)

# List comprehesion with condition
# with control logic [expression for item in iterable if condition]

lst= []
for i in range(10):
    if i % 2 ==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")

lst= []
for i in range(10):
    if i % 2 ==0:
        lst.append(i)

print(lst)


even_nums =[i for i in range(10) if i%2==0]
print(even_nums)
      
# Create Nested List Comprehensions
#nested List Comprehension [expression for item1 in itarable1 for item in iterable2]

lst1 = [1,2,3,4,5]
lst2 = ['a','b','c','d','e']

lst3 =[[i,j] for i in lst1 for j in lst2]
print(lst3)

# list comprehension with fumction calls

words =['hello','world', 'python ', 'programming']
lenghts =[len(word) for word in words]
print(lenghts)