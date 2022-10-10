# Defining multi_dimensional_array using numpy array

import numpy as np

two_dimension = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)]);
print(type(two_dimension));
print(two_dimension.shape);
print(two_dimension.size);
print(two_dimension.dtype);

# Accessing 2d array

# By row :
row_one = two_dimension[0];
print(row_one);  # accessing row one : 1,2,3

row_two = two_dimension[1];
print(row_two);  # accessing row two : 4,5,6

# By coln :
col_one = two_dimension[:, 0];
print(col_one);

second_col = two_dimension[:, 1];
print(second_col);

third_col = two_dimension[:, 2];
print(third_col);
