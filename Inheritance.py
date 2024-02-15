#When we want to make a new class which have some properties which is similar in our existing class there
#we use the concept of inheritance means we just use the common properties of existing class and add
#some new properties to our new class
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showdetail(self):
        print(f"The name of employee is {self.name} and id is {self.id}")

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
    def language(self):
        print(f"{self.name} has id {self.id} and he is programmer who know {self.lang} language")
prog=Programmer("Talha",62,"Python")
prog.language()
emp_1=Employee("Talha",62)
emp_1.showdetail()

class Vehicle:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def horn(self,horn):
        self.horn=horn
        print(f"The vehicle {self.name} has a model {self.model} with color {self.color} and do {self.horn}")

class Car(Vehicle):
    def __init__(self,name,model,color,speed):
        super().__init__(name,model,color)
        self.speed=speed
    def detail(self):
        print(f"The car {self.name} has a model {self.model} with color {self.color} and speed {self.speed}")

vec=Vehicle("CD",2018,"Red")
vec.horn("Po Po")

car=Car("Corola",2023,"White","200Km/h")
car.detail()