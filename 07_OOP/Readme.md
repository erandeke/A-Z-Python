
## OOP in Python 

Structure of class 

`class Name:

 #Constructor to create the object of the class
   def __init__(self) :
   def method_1(self) :
   def method_2(self) : 
   
#create an object of the class
obj = Name();

#call the functions`


## Inheritance :

Syntax :

   `class Parent:

     //expression

   class Child(Parent):`

Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). 
Similarly, the existing class is a base class (or parent class).


## Encapsulation:

Encapsulation is all about restricting the access of the methods and variables 
to the outside world .

Syntax: Declaring the private variable is done using single _ or 
double __ attached as prefix to the variable 

## example 
`class Car:
   def __init__(self):
     self.__car_price = 100; `
Here __car_price is private and hidden from outside scope 
