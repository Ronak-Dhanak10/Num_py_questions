# Consider a generator function that generates 10 integers and use it to build an array
import numpy as np

def generate_integers():
    for i in range(10):
        yield i

# yield returns one value at a time

arr = np.fromiter(generate_integers(),dtype=int)
# generate_integers() is a generator function that yields integers from 0 to 9. np.fromiter() takes this generator and creates a NumPy array from the yielded values.
# np.fromiter() --> reads values from the generator

print(arr)