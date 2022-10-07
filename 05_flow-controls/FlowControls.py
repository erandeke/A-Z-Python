# If statement in python


num = 2;
if (num % 2) == 0:
    print("num is an even");

# if-else statement

if (num % 3) == 0:
    print("Num is  divisible by 3")
else:
    print("Num is not divisible by 3");

# if -else - if

if (num % 3) == 0:
    print("Num is divisible by 3");
elif (num % 2) == 0:
    print("Num is divisible by 2");
else:
    print("Num is neither divisible by 3 nor by 2");

# Nested if

if (num % 2 == 0):
    if (num < 3):
        print("Nested if executed");
    else:
        print("Condition didn't met");
else:
    print("num is not even");
