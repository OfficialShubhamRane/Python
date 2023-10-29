class Mammal:

    def walk(self):

        if str(isinstance(self, Dog)):
            print("Dog is Walking");
        elif str(isinstance(self, Cat)):
            print("Cat is walking");
        else:
            print("Mammal is walking");


class Dog(Mammal):
    pass;


class Cat(Mammal):
    pass;


objDog = Dog();
objCat = Cat();

objCat.walk();
objDog.walk();
