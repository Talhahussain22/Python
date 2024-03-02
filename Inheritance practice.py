class Animal:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

    def show(self):
        print(f"The name of animal is {self.name} and gender is {self.gender}")

class Cat(Animal):
    def __init__(self,name,gender,colour,age):
        super().__init__(name,gender)
        self.colour=colour
        self.age=age

    @staticmethod
    def sound():
        print("Meo")
    def show(self):
        print(f"The name of cat is {self.name} and gender is {self.gender}  and colour is {self.colour} and age is {self.age} years")

a=Animal("Dog","Male")
a.show()
c=Cat("Tonny","Male","Black",3)
c.show()
c.sound()