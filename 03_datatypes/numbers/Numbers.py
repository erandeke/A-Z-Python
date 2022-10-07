# Numbers --> int , float and  complex

a = 3;
print(type(a));

b = 2.0;
print(type(b));

# Type Conversion

# one type can be converted into another
a = 1 + 2.0;
print("Converted to float", a)  # Converted to float 3.0

# calculations of float and decimals

var = 1.1 + 2.2;  # calculations done using float is an infinite long and approximate
print(var)  # 3.3000000000000003

# To solve the infite long precession , python has decimal
from decimal import Decimal as D

var = D('1.1') + D('2.2');
print(var);  # 3.3

var_1 = 1 / 3;
var_2 = 1 / 3;
print(var_1 + var_2);

from fractions import Fraction as F

var_1 = F('1/3');
var_2 = F('1/3');
print(var_1 + var_2);  #2/3
