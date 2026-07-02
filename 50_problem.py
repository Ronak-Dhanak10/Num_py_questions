# How to find the closest max value(to a given scalar) in a vector ?

import numpy as np 
arr = np.array([10,20,30,40,50])
value = 41

closet_max = arr[arr >= value].min()
print(closet_max)