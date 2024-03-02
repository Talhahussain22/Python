# #Sometimes we need to call fuction without actually giving parethesis in that case we use concept of
# #Getter which is denoted by @property which is actually a decorator
# # class MyClass:
# #     def __init__(self,value):
# #         self.val=value
# #     def show(self):
# #         print(f"The value is {self.val}")
# #
# #     @property
# #     def new_value(self):
# #         return  10 * self.val
# # obj=MyClass(20)
# # obj.show()
# # print(obj.new_value)
#
# class MyClass:
#     def __init__(self,value):
#         self.val=value
#     def show(self):
#         print(f"The value is {self.val}")
#
#     @property
#     def new_value(self):
#         return  10 * self.val
#
#     @new_value.setter
#     def new_value(self,change_value):
#         self.val = change_value/10
# obj = MyClass(20)
# obj.new_value=67
# obj.show()
# print(obj.new_value)
#
#
#

#As we have seen by changing value of first name email is not affecting so we have to use concept of propertry
#decorator here so that we create a new method name email but in code we don't have to add parethesis to call
# it that is reason we use property method on which it fell like we are dealing with attribute not with function
class Employee():
    def __init__(self,first,last):
        self.fir=first
        self.las=last
        # self.email=self.fir+self.las+"@gmail.com"

    @property
    def email(self):
        return self.fir + self.las + "@gmail.com"

    @property
    def full_name(self):
        return self.fir+self.las
    @full_name.setter
    def full_name(self,name):
        first,last=name.split()
        self.fir=first
        self.las=last
emp = Employee("Talha","Hussain")
emp.full_name="Farhan Zafar"
print(emp.fir)
print(emp.email)
print(emp.las)
print(emp.full_name)

