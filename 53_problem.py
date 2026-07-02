# How to convert a float (32 bits) array into an integer (32 bits) array in place?

import numpy as np
arr = np.array([1.5, 2.3, 3.7], dtype=np.float32)
print("Original array:", arr)
arr = arr.astype(np.int32)

print("Converted array:",arr)