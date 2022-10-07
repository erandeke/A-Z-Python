def welcome(name):
    """
    This function welcomes to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". welcome")


welcome('John')


def test():
    print("Dummy function");


test();


# Return statement

# program to return 1 for odd input and 0 for even input

def testEvenOrOdd(num):
    if num % 2 == 0:
        return 0;
    else:
        return 1;


print(testEvenOrOdd(10));

# scope of variables

global x;
x = 20;


def test():
    x = 10;  # local scope of x
    print("The value of x inside the function", x);


print("The value of x outside the function", x);
test();

# program to modify global var from inside the function


x = 2;  # global variable


def fun():
    # x = x * 2;  This will give unresolved reference error
    global x;
    x = x + 2;
    print(x);


fun();



# program to add two numbers


def add(x, y):
    sum = x + y;
    print("Add two numbers", sum);


add(10, 20);


# Define function with aribitary arguments

def welcomeAll(*names):
    for name in names:
        print("Welcome", name);


welcomeAll("John", "Mac", "Ron");
