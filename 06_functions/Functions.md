## Defining function in python

`def fun():   //defining function
//logic
func()   // to call function
`

## Scope of variables

## local scope

The variables have local scope and global scope

local scope : Variables that are defined inside the function and lifetime is only inside the execution of that
function .

`def func():
x = 10 //local`

Global scope : Variables that are defined outside the function and does not depend on function execution lifetime

## Arbitary Arguments :

When we are not sure of how many arguments we need to pass to function , we can use arbitary arguments in Python

  `def func(*text):
         //logic

  func("text1","text2","text3")
`

## Lambda function 

lambda function is just like any normal python function, except that it has no name when defining it, and it is contained in one line of code.

`lambda argument(x) : expression`
A lambda function evaluates an expression for the argument . Give the expression, 
it will evaluate and return the ans

example 

`def add(x):
   return x+x;`

using lambda :

`lambda x: (x+x);`

## Filter inbuilt function 

It is for filtering the elements based upon certain criteria

`list = [1,2,3,4,5,6,7,8]; //filter even elements 
filter(lambda x: (x%2 == 0),list);`

Syntax :
`filter(function, iterable) `
iterable can be any sort of data structure :list, dict, tuple 

## Map function:

This is another inbuilt python library with the syntax map(function, iterable).

## Modules :
A module is a file containing set of functions or codes that can be imported into another file 

creation of module 
`#module.py
def generate_welcome_msg(*names):
    for name in names:
        print("Hi" + " " + name + " " + "Welcome to the python dev club");`

importing module 
`#main.py
from module import generate_welcome_msg as msg, getMeSnacks as snacks;
msg("kedar", "kate", "croay");`


