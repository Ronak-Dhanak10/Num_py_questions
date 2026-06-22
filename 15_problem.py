# Create a 5×5 diagonal matrix with the values 1, 2, 3, 4, and 5 on the main diagonal using NumPy.
import numpy as np 
arr = np.diag([1,2,3,4,5],k=0)
print(arr)
# k=0	Main diagonal
# k=1	First diagonal above the main diagonal
# k=2	Second diagonal above the main diagonal
# k=-1	First diagonal below the main diagonal
# k=-2	Second diagonal below the main diagonal