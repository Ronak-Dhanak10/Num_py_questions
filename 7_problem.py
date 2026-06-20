#Create a 3x3 matrix with values ranging from 0 to 8
import numpy as np
arr = np.array((([0,1,2],[3,4,5],[6,7,8])))
print(arr)# THIS is done manually
matrix = np.arange(0,9).reshape(3,3)
print(matrix)# by methods
