# Catch  Exception:

import sys;

list = [1, 2, 4, 5];

for a in list:
    try:
        a / 0;
    except:
        print("Exception occurred", sys.exc_info()[0]);
        print();

# Handle Specific exceptions
import math

val = -10;
num = 1;
try:
    print(math.sqrt(val))  # Value error
    1 / 0;  # ZeroDivisionError
except(ZeroDivisionError, ValueError):
    print("Exception caught", sys.exc_info()[0]);



# Raising an exception
num = -1;
try:
    if num < 0:
        raise ValueError("Num is negative");
except(ValueError) as ve:
    print("Value error occurred", ve);
finally:
    print("I am executed");
