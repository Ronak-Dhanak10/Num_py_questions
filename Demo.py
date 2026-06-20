import numpy as np 
from scipy import stats 
data = [10, 20, 20, 30, 40, 50, 60] 
print(f"Mean: {np.mean(data)}") 
print(f"Median: {np.median(data)}") 
print(f"Mode: {stats.mode(data, keepdims=True).mode[0]}") 
print("HARSHENDRA SINGH") 
