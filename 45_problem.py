# Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area
import numpy as np

arr = np.zeros((5,5), dtype=[('X',int), ('Y',int)])

arr['X'], arr['Y'] = np.meshgrid(np.linspace(0,100,5),np.linspace(0,100,5))
print(arr)

# meshgrid() --> Return coordinate matrices from coordinate vectors