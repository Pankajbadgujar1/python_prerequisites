"""
Iterators: 
Iterators are advanced python concepts that allows for efficient looping and memory management .
Iterators provide a way to access elements of a collection sequentially without exposing the underlying structure.

"""
my_list = [1,2,3,4,5,6]
print(type(my_list))
print(my_list)

iterator = iter(my_list)
print(type(iterator))
print(iterator) #it create object obly

for i in iterator:
    print(i)