
# Creating dict is datastructure that holds key:value pair
# Key should be immutable like String,numbers, tuple
dict = {1: 'apple', 2: 'pine'};
print(dict);  # {1: 'apple', 2: 'pine'}

# creating dict with tuple as value
dict = {1: (1, 8), 2: (8, 9)};
print(dict);  # {1: (1, 8), 2: (8, 9)}

# creating dict with mixed keys
dict = {1: 'apple', 2: [1, 2, 3]};
print(dict)  # 1: 'apple', 2: [1, 2, 3]}

# Accessing the elements in dict
# 1) using sqaure brackets - This will throw an error if the key is not found
# 2) get() - this will give None if the key is not present

dict = {1: 'apple', 2: "pine"};
print(dict[1]);  # applle

# using get()
print(dict.get(2));  # pine

# using get() when the key is not found
print(dict.get(6));  # none

# Updating the dictionary

dict = {1: 'apple', 2: 'pine'};
dict[1] = 'pears';
print(dict)  # {1: 'pears', 2: 'pine'}

# Adding new record set to dictionary

dict[3] = 'orange';
print(dict);  # {1: 'pears', 2: 'pine', 3: 'orange'}

# Remove an item from dictionary

dict = {1: 'apple', 2: 'pine', 3: 'orange'};
dict.pop(1);
print(dict);  # {2: 'pine', 3: 'orange'}

# flushing the dict
dict.clear();
print(dict);

# Dictionary comprehension : To create the dictionary from an iterable in python

dict = {x: x for x in range(5)};
print(dict);  # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
