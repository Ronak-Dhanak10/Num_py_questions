# Create array with negetive sign value than remove the sign and than sort and then Unique sorted array print

import numpy as np 
arr = np.random.randint(-20, 20, (15))
print("Original array:", arr)

arr1 = np.abs(arr)
print("Sign Remove:",arr1)

arr2 = np.sort(arr1)
print('Sort A',arr2)

arr3 = np.unique(arr2)
print("Unique sorted array:",arr3)
