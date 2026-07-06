# Create Histogram Using NumPy
# import numpy as np
# data = np.random.randn(1000)
# hist, bins = np.histogram(data, bins=10)
# print("Histogram:", hist)
# print("Bins:",bins)
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data, bins=10, edgecolor='black')
plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)

plt.show()