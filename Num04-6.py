import numpy as np 
import time
 

size = 10000000

py_list = list(range(size))
start = time.time()
sq_list = [x**2 for x in py_list]
end = time.time()
print(f"python list time = {end-start} seconds ")

np_arr = np.array(py_list)
start = time.time()
sq_arr = np_arr **2
end = time.time()
print(f"numpy array time ={end-start} seconds")