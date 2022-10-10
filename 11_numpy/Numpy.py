# Program related to numpy

import numpy as np

# checking version of numpy
print(np.__version__);

# Create array using numpy from list

list = [1, 2, 3, 4];
numpy_array = np.array(list);
print(numpy_array);

# Creating array using numpy

arr = np.array([1, 2, 3, 4], dtype=int);
print(arr);

# creating float array from list of float

float_list = [1.2, 3.4, 4.5];
print(np.array(float_list));

# creating a multidimensional array

multi_dimensional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
d_list = np.array(multi_dimensional_list);
print(d_list);

# Creating an numpy array  from tupple

tuple = (1, 2, 3);
np_array = np.array(tuple);
print(np_array);
print(type(np_array));

# shape of the numpy array

arr = np.array([1, 2, 3]);
print(arr.shape);  # for dimensional it returns the size of the elements

arr_two_dimensional = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3]]);
print(arr_two_dimensional.shape);  # 3,3

# size of the numpy array

one_d_array = np.array([1, 2, 3]);
print(one_d_array.size);  #3

