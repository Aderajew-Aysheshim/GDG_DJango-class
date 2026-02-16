from abc import ABC, abstractmethod

class Animal(ABC): #
    @abstractmethod
    def make_sound(self): #
        pass

class Dog(Animal): #
    def make_sound(self):
        return "Woof!"

class Cat(Animal): #
    def make_sound(self):
        return "Meow!"

# Demonstrate polymorphism by calling make_sound() using a parent reference
animals = [Dog(), Cat()] # List of objects from different classes
for animal in animals:
    print(animal.make_sound()) # Calling a common method
