# Type Error : This ocurrs when we try to access the data giving incorrect data type as below

# Type error om accessimg set using index

set = {1, 2, 3};
print(set[0]); #'set' object is not subscriptable

str = "code";
print("Incorrect index used hence Type Error", str[1.5])  # string index must be integer

# string are immutable in nature , You cannot change the character or delete it

str_immutable = "Kedar";
str_immutable[1] = "a";
print("Will string allow this replacement", str_immutable);  # string object does not support item assignment

tup = (1, 2, 3);
tup[0] = 1;
print(tup);  # 'tuple' object does not support item assignment
