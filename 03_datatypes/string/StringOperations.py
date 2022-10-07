# Concatenation: Operation to append the string

str1 = "hello";
str2 = "world";

print("Concatenated String", str1 + str2);  # helloworld

# Repeat the string
print("String repetition", str1 * 3);  # hellohellohello

# We can check if string is part of another string

str1 = "a";
str2 = "apple";
print(str1 in str2);  # True

# Built in functions

# 1) len  : It is used to calculate the length of string
# 2) enumerate : It is use to get the characters and their index from the string


str = "Kedar";
print("The length of the string is", len(str));  # 5

print("Enumerate the string to get the index",
      list(enumerate(str)));  # [(0, 'K'), (1, 'e'), (2, 'd'), (3, 'a'), (4, 'r')]

# String escaping
# Hi , "What's up?"

# 1)using multiline
print(""" Hi , "What's up" ?""");

# 2) using backslash
print("Hi , \"What's up?\"");

# Using String format

format_1 = "{},{}".format("Kedar", "Erande");
print("String formatted with format function", format_1);  # Kedar,Erande

format_repeat = "{} and {}".format("Tic", "Toe");
print(format_repeat);  # Tic and Toe

format_2 = "{k} {e}".format(k="Kedar", e="Erande");
print(format_2)  # Kedar Erande

# 3) using lower and upper

print("KEDAR".lower());  # kedar

print("kedar".upper());  # KEDAR

# 4)Split
str = "Hi how are you";
print("Lets split the string", (str.split()));  # "Hi","How","are","you"

# 5)replace
str = "Coding in python is fun";
print("Let's replace fun by great", str.replace('fun', 'great'))  # coding in python is great

# 6) strip func : It removes leading and tailing characters
str = " Kedar ";
print("Strip will remove first and tailing character", str.strip());
