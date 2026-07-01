# Create a random vector of size 10 and sort it
import numpy as np 

arr = np.random.randint(1,50,(10))
print("Original array:", arr)

print("Sortedarray:",np.sort(arr))