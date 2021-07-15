class Person:

    def __init__(self, name):
        self.name = name;

    def talk(self, name):
        print(f"{name} is talking...");


obj = Person("Shubham");
obj.talk("Shubham");