

## Catching Exceptions in Python 

Syntax of exception handling :

`import sys //This is to give name of exception
try:
  //exception might occur
except:
  //this is the catch block to handle exceptions
  // print("Exception occurred",sys.exc_info[0]);`


## Catching Specific exception

`try:
 //exception raised:
except(ZeroDivisionError, ValueError):
 //print 
`

## Raising an exception :

Syntax:

raise MemoryError("Error raise");

Code sample:

`num = -1;
try:
    if num < 0:
        raise ValueError("Num is negative");
except(ValueError) as ve:
    print("Value error occurred", ve);`
Op: Value error occurred Num is negative


## Try with finally 

This clause is executed in all cases no matter what and it is used for 
freeing up the resources 

code sample :
`try :
 //exception occurred or not 
except:
 //caught exception
finally:
 //cose db connection`

## User Defined Exception

These are the custom exceptions built based upon business usecase.
_`Code in : InsufficientBalanceException.py_ `

