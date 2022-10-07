# Design polymorphism (having multiple forms ) using an interface


def poly_interface(bird):
    bird.fly();


class Parrot:
    def fly(self):
        print("Parrot files");


class Crow:
    def fly(self):
        print("Crow flies");


p1 = Parrot();
c1 = Crow();

poly_interface(p1);  # Parrot flies

poly_interface(c1);  # Crow flies
