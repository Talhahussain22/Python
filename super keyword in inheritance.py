#super keyword is used to use methods in child class that are defined in parent class:
class Vehicle():
    def __init__(self,name,colour,model):
        self.name=name
        self.colour=colour
        self.model=model

    def greet(self):
        print("Welcome to my store!")

class Car(Vehicle):
    def __init__(self,name,colour,model,roof):
        super().__init__(name,colour,model)
        self.roof=roof
    def greet(self):
        print("Hello world!")
    def check(self):
        print("This is child class")
        super().greet()
c1=Car("Corola","REd",2019,"closed")
c1.check()