# create a class

class Engineer:

    def __init__(self, name, age):  # This is an initializer method that runs first as soon as object is
        # created
        self.name = name
        self.age = age


# instantiate the Engineer class
e1 = Engineer("Rock", 30);
e2 = Engineer("James", 20);

# accessing the class attributes
print("{} is an Engineer having age {}".format(e1.name, e1.age));


# create a class with custom methods

class Driver:

    def __init__(self, name, place, carNum, carModel):
        self.name = name;
        self.place = place;
        self.carNum = carNum;
        self.carModel = carModel;

    def drive_car(self, place):
        return "{}, this is current location".format(place);

    def register_car(self, carNum, carModel):
        return "{} registered success with car model as {}".format(carNum, carModel)


d1 = Driver("Rock", "LA", "LA123US", "AS-TU");
print(d1.drive_car("MView"));
print(d1.register_car("US", "123"))


# Design class student with student profile details

class Student:

    def __init__(self, name, age, rollNo):
        self.name = name;
        self.age = age;
        self.rollNo = rollNo;

    def enroll(self, name):
        return "Student {}" + name + "got enrolled";

    def saveStudent(self, name, age, rollNo):
        return " Student with following details got saved" \
               + "   " + "name::" + name + "   " + "rollNo::" + rollNo + "  " + "age::" + age;

std = Student("Roc", "10", "100");

# saveStudent
print(std.saveStudent("Roc", "10", "100"))
