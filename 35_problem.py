# Create a vector of size 10 with values ranging from 1 to 100, both excluded
import numpy as np 

arr = np.linspace(1,100,12)[1:-1]

print(arr)

# linspace()  --> Returns evenly spaced numbers over a specified interval
# [1:-1]  --> Excludes the first and last elements of the array