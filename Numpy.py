import numpy as np
import time
# arr = np.array([1,2,3,4,5])
# print(arr,type(arr))
size = 100_00_000

# python list
py_list = list(range(size))
start = time.time()
sq_list =[x**2 for x in py_list]
end = time.time()
print(f"Timetaken for python list: {end - start:.2f} seconds")
# numpy array
np_array = np.arange(size)
start = time.time()
sq_array =np_array ** 2
end = time.time()
print(f"Timetaken for numpy array: {end - start:.2f} seconds")  