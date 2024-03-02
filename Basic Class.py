# # Class is like a blue print which hold some variable which can be modified later on by using methods:
# # Class is made  so we use it again and again instead of creating variable again or reduce duplication of variable
# class Student:
#     name = "Talha"
#     occupation = "Software engineer"
#     Year = "1st"
#     Roll_number = 62
#
#     def info(self):
#         print(f'His name is {self.name}')
#
#
# a = Student()
# b = Student()
# a.name = "Tayyab"
# b.name = "Ali"
# a.info()

#As we seen above while making any class we are storing some variable in it instead of that if we want to
#directly use a way in which we don't have to store this variable so we can directly give argument and it take
# it position for that we use concept of contructors..

# class Person:
#     def __init__(self,name,occupation):
#         self.name=name
#         self.occ=occupation
#
#     def info(self):
#         print(f'{self.name} is a {self.occ}')
# a=Person("Talha","Software_Developer")
# b=Person("Ali","HR")
# a.info()
# b.info()
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f'{self.name} is {self.age} year old')

a = Person("Talha",18)
b = Person("Ali",19)
# a.info()
# b.info()
