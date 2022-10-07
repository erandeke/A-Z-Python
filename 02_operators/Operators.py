# Intro to python
# Basic operations

# ADD

print("Addition", 2 + 3);  # 5

# SUB

print("Subtraction", 3 - 2);  # 1

# DIV
print("DIVISION", 3 / 2);  # 1.5

# MULT
print("MULTIPLY", 3 * 2);  # 6

# exponent
print("EXPONENT", 3 ** 2);  # 9

# Mod
print("MOD", 3 % 2)  # 1

# Floor div
print("DIVISION WITHOUT REMAINDER", 3 // 2)  # 1 - rounded to nearest

# Arithmetic operations :

a = 10;  # a is variable and it has Integer data type
b = 20;  # b is variable and it has Integer data type

total = a + b;
floor_div = b // a;
remainder = a / b;
product = a * b;

print("Add total", total);
print("floor_div", floor_div);
print("remainder", remainder);
print("product", product);

# Operations of INTEGER AND FLOAT

sum = 10 + 10.2;
print(sum); #casted into float (20.2)

# boolean funcs:

# '>' -> greater than
# '>=' -> greater than or equal to
# '<' -> lesser than
# '<=' -> lesser than or equal to
# '=='  -> equals
# '!=' -> Not equals

# Boolean comparisons

print(len("kedar") == len("kedar"));  # true
print(3 > 2);  # true
print("True is equal to True :", True == True);  # true

print('1 is 1', 1 == 1)  # true

# Number comparisons

print(3 < 4 and 4 > 5);  # false
