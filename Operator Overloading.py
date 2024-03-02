#Operator overloading means that we use operator more than its actual use means + operator generally used for not only
#adding intergers but also two str and merge two list this is because the + operator is overload means str and list
#class defined + operator used differntly we can aslo defined in our class what we want to acheive by method of overloading
# as we used + operator for adding vectors and * operator for calculation their dot product.
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,v2):
        return Vector(self.i+v2.i ,self.j+v2.j ,self.k+v2.k)

    def __mul__(self, other):
        return self.i*other.i+self.j*other.j+self.k*other.k

v1=Vector(3,5,7)
v2=Vector(1,6,3)
print(v1+v2)
print(v1*v2)


