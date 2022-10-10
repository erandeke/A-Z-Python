import numpy as np;

# Convert int to float

list = [1, 2, 3, 4];
print(np.array(list, dtype='float'));

# Convert float to int
numpy_arr = np.array([1.2, 2.3], dtype=int);
print(numpy_arr)

# Convert int to boolean
num_into_boolean = np.array([-1, 1, 0, -2, 10],dtype=bool);
print(num_into_boolean)