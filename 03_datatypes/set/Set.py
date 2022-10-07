# Set is an unordered collection . It is mutable . It is also used to perform mathematical operations like
# union, intersection , etc


# Create sets
# Set in python is created by placing all the items in curly braces

# Initialize an empty set

set = set();
print(type(set));  # <class 'set'>

set = {1, 4, 3};
print("Set", set);  # 1,3,4

# Set of mixed data types
set = {"Kedar", 1.5, "hash"};
print("Set of mixed type", set);  # {1.5, 'Kedar', 'hash'}

# Set cannot have an duplicate
set = {1, 2, 2, 3};
print("Set cannot have an duplicate", set);  # {1, 2, 3}

# sets are unordered collection hence indexing will not make sense here , so it does not support indexing
# check more on TypeError when you access the set using indexing

# Add elements to set

set = {1, 4, 5};
set.add(6);  # Add supports only addition of one element
print("Adding an element to set", set);  # {1, 4, 5, 6}

# Adding multiple elements in the set
set = {1, 6, 7};
set.update(["Kedar", "Code"]);
print("Adding multiple elements to the set", set);  # {1, 'Kedar', 6, 7, 'Code'}

# Adding tupple, list to set
set = {1, 2};
t1 = (6, 7);
list = ["rock", "shawn"];
set.update(t1, list);
print("Updating set with tuple and list", set);  # {1, 2, 6, 7, 'rock', 'shawn'}

# Removing elements from the set

# 1)Discard : This is safe removal , it won't raise an error if the item is not in the set
# 2)Remova : This method will raise an error if an item is not found in the set (refer keyError in error pkg)

set = {9, 7, 8};
set.discard(7);
print("Discarding 7 from set", set);  # 8,9

# If the item is not present in set using discard
set.discard(100);
print("No exception", set);  # 8,9

# Flushing all the elements from set

set = {0, 0, 1};
set.clear();
print("Flushed set", set); # set(); empty set
