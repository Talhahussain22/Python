#dir is used to find methods that a particular class have:
x=[]
print(dir(x))
y=()
print(dir(y))
z={}
print(dir(z))

#__dict__ is use to check all attributes associated with particular instance
class Fun():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary


p=Fun("Talha","19",20000)
print(p.__dict__)

#help method explain more about a particular class
print(help(Fun))