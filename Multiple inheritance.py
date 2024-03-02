class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance=dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Dancer,Employee):
    def __init__(self,name,dance):
        self.name=name
        self.dance=dance

de=DancerEmployee("Haris","Breakdance")
print(de.name)
print(de.dance)
de.show()
#The thing is that when we inherit multiple classes the class whose method like here (show) get priority which is given
#as first argument the level of priority can be check by (.mro) method[<class '__main__.DancerEmployee'>, <class '__main__.Dancer'>, <class '__main__.Employee'>, <class 'object'>] the first priority will be current class it will
#check if method does'nt exists then it will check in parent class which is first argument is does'nt exists it will
#check 2nd argument if not exists and there is not argument it will through error

print(DancerEmployee.mro())
