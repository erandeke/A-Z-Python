# Single line

str = "Kedar";
print(str);

# print length of string
print(len(str))

# multiline String

str_multiline = '''
Hi Kedar ...lets learn to code
in python
'''
print(str_multiline);

# Access the characters in String using indexing and slicing

# index is 0 based in Python

str_char = "machine-learning";

print("Get me first character that starts with index 0", str_char[0]);

print("Get me second character that starts with index 1", str_char[1]);

# To access last character in python index starts with -1 , second_last : -2

print("Get me last character that ends of string which has index -1", str_char[-1]);  ## g

print("Get me second last character that has index -2", str_char[-2]);  ## n

# Slicing
# If we want to access the substring between the certain range then slicing comes handy

print("Slice string machine-learning from 1:5", str_char[1:5]);  ## achi

print("Slice string machine-learning from 1: end", str_char[1:]);  ## achine-learning

# Tailing characters slicing

print("Slice string machine-learning for tailing order from -4 to -1", str_char[-4:-1]);  # nin

# delete String

str_demo = "hello world";
del str_demo;  #This action will entirely delete the string
print(str_demo);
