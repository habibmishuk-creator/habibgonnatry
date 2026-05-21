class Animal:
    #constructor
    def _init_(self, name):
        self.name = name
        print("Animal Constructor")

    def eat(self):
        print(self.name + " eats it")

class Dog(Animal):                      #new class(child class-Dog) that inherits the attributes from parent class(Animal)
    def _init_(self, name):
        super()._init_(name)          #Parent class constructor

        print("Dog Class Constructor")

    def bark(self):
        print(self.name + " barks it")

class cat(Animal):
    def _init_(self, name):
        super()._init_(name)
        self.name = name
        print("Cat Class Constructor")

    def meow(self):
        print(self.name + " meows it")

dogname = input("Enter the dog name: ")
catname = input("Enter the cat name: ")

d1 = Dog(dogname)
c1 = cat(catname)
d1.eat()
d1.bark()
c1.eat()
c1.meow()