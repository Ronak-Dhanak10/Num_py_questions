# How to sort an array by the nth column?
import numpy as np

Z = np.array([
    [5, 2, 3],
    [1, 4, 6],
    [7, 0, 9]
])

n= 1 # sort by the second column (index 1)
# O/P depends only 2nd column.short the array according to 2nd column
print(Z)
Z = Z[Z[:, n].argsort()]

print(Z)