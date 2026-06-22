# How to add a border (filled with 0's) around an existing array?
import numpy as np 
arr =np.array([[1,3,2,5,4],[6,4,2,3,7],[1,5,9,3,4],[9,5,1,3,6],[7,5,3,4,1]])
arr  [0,:] = 0
arr  [-1,:] = 0
arr  [:,-1] = 0
arr  [:,0]  = 0
print(arr)