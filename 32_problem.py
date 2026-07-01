# Extract the integer part of a random array of positive numbers using 4 different methods
import numpy as np 
arr = np.random.uniform(0,10,(10))
print("Original array:",arr)

print("Method one:",arr.astype(int))
# astype(int) --> Convert the array to integer type, effectively truncating the decimal part

print("Method Two:",np.trunc(arr))
# np.trunc() --> Truncates the decimal part of each element in the array

print("Method Three:",np.floor(arr))
# np.floor() --> Returns the largest integer less than or equal to each element

print("Method Four:",arr -arr%1)