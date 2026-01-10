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

arr1 = np.array([1,2,3,4,5])
print(arr1)

print(type(arr1))
print(arr1.shape)

#Convert array in rows and colmns

arr2 = np.array([1,2,3,4,5])
print(arr2.reshape(1,5)) # 1 row and 5 column

arr2 = np.array([[1,2,3,4,5],[11,22,33,44,55]])
print(arr2)
print(arr2.shape)

arr3 = np.array([1,2,3,4,5,6,7,8,9])

print(arr3.reshape(3,3))
print(arr3.shape)

print(arr3)

a = np.ones((3,4)) # 3 row and 4 columns
print(a)


## Numpy vectorize operations

arr5 = np.array([1,2,3,4,5,6,7,8])
arr5 = np.array([10,20,30,40,50,60,70,80])

print("Addition :",arr1+arr2)