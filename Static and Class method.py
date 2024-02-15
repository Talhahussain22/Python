# # Static method is used when we want to make method in a class that does'nt need any object refrence
# #we do this to so that we can use this method withint class also when we want to mutliple functions
# # to use in other python file we make class with those fuctions with static method so that we don't have
# #to make object to run those methods..
#
# class Math:
#     def __init__(self,num):
#         self.num=num
#
#     @staticmethod
#     def add(a,b):
#         return a+b
#
#     print(add(1,2))
#
#
# c=Math(6)
# print(c.add(3,4))
#
# class Dogs:
#     dogs=[]
#     a="mony"
#     def __init__(self,name):
#         self.name=name
#         self.dogs.append(self.name)
# dog=Dogs("tony")
# dog.name="Tim"
# print(dog.name)
# dog_1=Dogs("Jaccky")
# print(dog.dogs)

#whenever we change any property say we made a function changecompany which will change company name that
#is already defined if I try to change it will change for particular instance but the class variable will
#not change to change class variable we use this class decorator above the function that changing company's name
class Employee:
    company="Apple"
    def show(self):
        print(f'The name of employee is {self.name} and company is {self.company}')
    @classmethod
    def changecompany(cls,name):
        cls.company=name
e1=Employee()
e1.name="Talha"
e1.changecompany("Samsung")
e1.show()
print(Employee.company)
