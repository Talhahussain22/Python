def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using my Function")
    return mfx()
@greet
def hello():
    print("Hello World")

def greet2(fg):
    def mfg(*args,**kwargs):
        print("Good Morning")
        fg(*args,**kwargs)
        print("Thanks for using")
    return mfg
@greet2
def add(a,b):
    print(a+b)
add(2 , 4)
