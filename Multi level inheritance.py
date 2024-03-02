class Human:
    def __init__(self,name,age,religion):
        self.name=name
        self.age=age
        self.religion=religion

    def show(self):
        print(f"The name is {self.name} and age is {self.age} and religion is {self.religion}")

class Employee(Human):
    def __init__(self,name,id,designation,age,religion):
        Human.__init__(self,name,age,religion)
        self.id=id
        self.designation=designation

    def show(self):
        Human.show(self)
        print(f"{self.name} has id {self.id} with designation of {self.designation}")

class Programmer(Employee):
    def __init__(self,name,id,designation,language,age,religion):
        Human.__init__(self,name,age,religion )
        Employee.__init__(self,name,id,designation,age,religion)
        self.language=language

    def show(self):
        Employee.show(self)
        print(f"{self.name} is a Programmer with  designation {self.designation} and know {self.language} language")

p=Programmer("Talha",62,"Senior developer","Python",18,"Islam")
p.show()