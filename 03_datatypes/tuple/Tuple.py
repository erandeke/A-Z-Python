# Tuple in python is same as that of list only thing is that tuple is immutable

# Tuple holding integers

t1 = (1, 2, 3);
print(t1);  # 1,2,3

# Tuple with mix data types
t1 = ("Kedar", 2);
print(t1);  # 'Kedar' , 2

# Nested tuples

t1 = ((1, 2, 3), [1, 4, 5]);
print("Nested tuples", t1);  # ((1, 2, 3), [1, 4, 5])

# Accessing the tuples

tup = (1, 2, 3);
print("0 the element", tup[0]);  # 1

# Changing the items in tuple

# 1)Tuple is immutable hence its values cannot be changed (see more in exceptions package)

# 2) If the items used in tuple are of list types then it can be changed

tuple = ((1, 2, 3), [1, 3]);
tuple[1][0] = 7;
print("Changing tuple holding list items", tuple);  # ((1, 2, 3), [7, 3])

# Deleting tuple : Since its immutable , deleting an item in tuple is not possible.
# However we can delete the entire tuple
t1 = (90,);
del t1; #this will delete the tuple
