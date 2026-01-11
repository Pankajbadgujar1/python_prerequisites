"""
numpy = Numeric python 
NumPy (Numerical Python) is a fundamental library for scientific computing in Python, primarily used for its efficient 
multi-dimensional array object called ndarray. It is significantly faster than standard Python lists for numerical tasks
 because it stores data in contiguous memory blocks and uses optimized C-based code for operations. 

The primary uses of NumPy in Python include:
Efficient Array Manipulation: Creating, reshaping, stacking, splitting, and indexing large, multi-dimensional arrays
 (matrices/tensors) of homogeneous data types.

Mathematical and Logical Operations: Performing element-wise operations (addition, subtraction, multiplication, division), 
as well as complex mathematical functions (trigonometry, exponentiation, logarithms, square roots) on entire arrays without
 explicit Python loops (vectorization).

Linear Algebra: Providing a robust set of routines for advanced linear algebra operations, such as matrix multiplication,
 determinants, inversion, and solving linear systems.

Statistical Analysis: Offering built-in functions for statistical calculations, including mean, median, variance, 
standard deviation, and more.

Random Number Generation: Providing modules for generating random numbers and working with various probability 
distributions (normal, uniform, etc.), which is essential for simulations and machine learning.

Integration with Other Libraries: Serving as the foundational data structure for many other major data science and machine
 learning libraries, such as Pandas, SciPy, Matplotlib, and scikit-learn. 

In essence, NumPy provides the performance and functionality needed to handle large numerical datasets efficiently,
 making it an indispensable tool in data science, engineering, and scientific research. You can learn more about its 
 features and get started with tutorials on the official NumPy documentation. 
"""
import numpy as np
#create array using numpy
# 1 D array
arr1 = np.array([1,2,3,4,5])
print(arr1)

print(type(arr1))
print(arr1.shape) # Whenever there one dimentional array their is one number is available

#Convert array in rows and colmns
# 2D array
arr2 = np.array([1,2,3,4,5,8])
print(arr2.reshape(2,3)) # 1 row and 3 column

arr2 = np.array([[1,2,3,4,5],[11,22,33,44,55]])
print(arr2)
print(arr2.shape)

arr3 = np.array([1,2,3,4,5,6,7,8,9])

print(arr3.reshape(3,3))
print(arr3.shape)

print(arr3)


# Use of inbuld function np.ones() and np.zeros() 
# They give us 2D array 
a = np.ones((3,4)) # 3 row and 4 columns
zero = np.zeros((3,4))
print("\n\nPrinting Zeros :=\n",zero)


#Creating identical array
identical = np.eye(4,4)
print("\n\nThis is an identical array :-\n",identical)

#create array using the inbult function
arr4 = np.arange(0,20,4)
print(arr4)

print("Reshaping arr =\n ",arr4.reshape(5,1))


### Some more feature about np.array function
print("\n\nPrinting an attributes of array :")
arr = np.array([[1,2,3],[4,5,6]])
print("Array: \n",arr)
print("\nShape : ",arr.shape)
print("\nNumber of dimention : " , arr.ndim)
print("\nSize (Number of elements ): ",arr.size)
print("\nDatatype : ",arr.dtype)
print("\nItem size (in bytes ):",arr.itemsize)

## Numpy vectorize operations

arr5 = np.array([1,2,3,4,5,6,7,8])
arr5 = np.array([10,20,30,40,50,60,70,80])

print("\n\nAddition :\n\n",arr1+arr2)

# Unversal functions That applies to hole array
#Square Root function
print("Printing square roots",np.sqrt(arr),"\n\n")

#Exponentional function
print(np.exp(arr))

# Sine
print(np.sin(arr))

#natural log
print(np.log)

## Array Slicing and Indexing
print(arr)

# array indexing start from 0
print(arr[0][0]) # first element
print(arr[0:2,1:])

#modify the array elements

print(arr)
arr[1:]=100
print(arr)

# Statistical concepts -- Normalization
# TO have a mean of 0 and stardred deviation of 1

data =np.array([1,2,3,4,5])
#calculating meand and startdred deviation
mean = np.mean(data)
std_dev = np.std(data)

# normalize the data

Normalized_data= (data - mean) / std_dev

print("Normalized_data : ",Normalized_data)