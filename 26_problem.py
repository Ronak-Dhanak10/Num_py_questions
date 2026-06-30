# How to round away from zero a float array ?

import numpy as np
arr = np.array([1.2,-2.7,3.1,-4.9,0.1])

result = np.abs(arr)
result1 = np.ceil(np.abs(arr))
result2 = np.copysign(np.ceil(np.abs(arr)),arr)

print("Original Array:",arr)
print("Remove signs:",result)
print("Increase value Upward:",result)
print("Restor sign:",result2)

# np.abs(arr) --> Removes the signs temporarily
# np.ceil( ) --> rounds each value upward to the next integer
# np.copysign(  , arr) --> Restore original signs  