# Encapsulation is all about restricting the access of the methods and variables
# to the outside world .

class Car:

    def __init__(self):
        self.__car_price = 100;

    def setCarPrice(self, price):
        self.__car_price = price

    def get_car_price(self):
        return self.__car_price;


car = Car();
print(car.get_car_price());  # 100;

# try to chang the price
car.__car_price = 200;
print(car.get_car_price());

car.setCarPrice(200);
print(car.get_car_price());  #200
