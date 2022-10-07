# Program to inherit from Parent and child relationship
# Here child can see what Parent can do


class Parent:

    def __init__(self):
        print("I am the parent");

    def teachToChild(selfs):
        print("I can teach my child");

    def takeCare(self):
        print("I can take care of my child");


# Create child class inheriting Parent

class Child(Parent):

    def __init__(self):
        super().__init__();
        print("I am child");


c = Child();
c.teachToChild();
c.takeCare();
