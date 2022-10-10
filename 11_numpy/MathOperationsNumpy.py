import numpy as np;

# Addition:

np_array_list = [1, 2, 3, 4];
np_array = np.array(np_array_list);
print("Np array ", np_array);
print(np_array + 10);  # No need of iterating over the list

# Subtraction
np_array_sub = np.array([1, 2, 3, 4]);
print(np_array_sub - 1);  # this will subtract 1 from every element

# Multiplication:
np_array_mult = np.array([1, 2, 3, 4]);
print(np_array_mult * 2);  # this will multiply every number with 2

# Division
np_array_div = np.array([1, 2, 3, 4]);
print(np_array_mult / 2);

# Floor div
np_array_floor_div = np.array([1, 2, 3, 4]);
print(np_array_floor_div//2);


# Exponent
np_array_floor_expo = np.array([1, 2, 3, 4]);
print(np_array_floor_expo ** 2);