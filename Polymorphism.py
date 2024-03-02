#Polymorphism means using a thing more than once but with diff implementation. It could me a method like speak in below example.
#speak method in all classes which inherit from parent class (animal) have diff implementation.
#It has two main method like method overriding when we have done below in which child class alternation method of
#parent class but have same name and other is method overloading which we understood in C++ in which method with same
#name but diff type or number of argument behave differntly.
class Animal:
    def speak(self):
        return "Nothing"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Tweet!"

# Polymorphism
def animal_speak(animal):
    print(animal.speak())

animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal_speak(animal)

