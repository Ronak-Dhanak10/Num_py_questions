# How to tell if a given 2D array has null columns?

import numpy as np
arr = np.array([
    [1,0,3],
    [4,0,7],
    [9,0,5],
])
print((arr == 0).all(axis=0))
print(np.any((arr == 0).all(axis=0)))
print(np.where((arr == 0).all(axis=0))[0])