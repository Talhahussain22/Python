class Employee:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        count=0
        for i in self.name:
            count+=1
        return count

    def __str__(self):
        return f"The name of Employee is {self.name}"

