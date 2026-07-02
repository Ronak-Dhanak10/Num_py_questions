# Make an array immutable (read-only)
import numpy as np

Q = np.array([1, 2, 3, 4, 5])
Q.flags.writeable = False # Make the array ready only

print("Array Q:", Q)
