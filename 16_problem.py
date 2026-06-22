# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
import numpy as np 
arr = np.diag([1,2,3,4,5],k=-1)
print(arr)
# k=0	Main diagonal
# k=1	First diagonal above the main diagonal
# k=2	Second diagonal above the main diagonal
# k=-1	First diagonal below the main diagonal
# k=-2	Second diagonal below the main diagonal