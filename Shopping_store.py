class Admin():
    item_and_stock={"Bottle":50,"Glasses":100}
    item_and_price={"Bottle":200,"Glasses":500}
    def __init__(self,name,price,stock):
        Admin.item_and_stock[name]=stock
        Admin.item_and_price[name]=price

    @classmethod
    def update(cls):
        name=input("Name:")
        if name in Admin.item_and_price:
            while True:
                ask=input("What do you want to update?(P for Price ,S for Stock,B for both):")
                if ask.upper()=="P":
                    Admin.item_and_price[name]=input("New_Price:")
                    print(Admin.item_and_price)
                    break
                elif ask=="S":
                    Admin.item_and_stock[name]=input("New_Stock:")
                    break
                elif ask=="B":
                    Admin.item_and_price[name]=input("New_Price:")
                    Admin.item_and_stock[name]=input("New_Stock:")
                    break
                else:
                    print("Enter a valid character P,S,B")
        else:
            print("Item does'nt Exists")
    @staticmethod
    def show():
         print(f"The store has items and price {Admin.item_and_price} with item and stock {Admin.item_and_stock} ")
    @classmethod
    def remove(cls):
        name=input("Name:")
        if name in Admin.item_and_price:
            Admin.item_and_price.pop(name)
            Admin.item_and_stock.pop(name)
            print(f'{name} is Successfully removed')

        else:
            print("Item does'nt Exists")

class User:
    @staticmethod
    def buy():
        l=[]
        price=0
        i=0
        no_of_items=int(input("Enter number of items you want to buy:"))
        while i<no_of_items:
            item=input(f"Item{i+1}:")
            if item in Admin.item_and_price:
                if item not in l:
                    quantity=int(input("Quantity:"))
                    price+=Admin.item_and_price[item]*quantity
                    l.append(str(quantity)+item)
                    Admin.item_and_stock[item]-=2
                    i+=1
                else:
                    print("Item Already Purchased!")
            else:
                print("Item does'nt exists")
        print(f"You have bought {l} and you total bill is {price}")
Admin("Shoes",2000,25)
Admin("Clock",1500,35)
def call():
    while True:
        while True:
            try:
                check=input("You are admin or user:")
                break
            except Exception as e:
                print(e)
        if check.upper()=="ADMIN":
            password=int(input('Enter a password:'))
            if password==1234:
                print("Welcome To Shopping Store!")
                ad_ask=input("Do you want to update,remove,show (U,R,S):")
                if ad_ask.upper()=="U":
                    Admin.update()
                    break
                elif ad_ask.upper()=="S":
                    Admin.show()
                    break
                elif ad_ask.upper()=="R":
                    Admin.remove()
                    break
            else:
                print("INVALID PASSWORD")
        elif check.upper()=="USER":
            print("Welcome to Shopping Store!")
            User.buy()
            break
        else:
            print("Enter valid word(user or admin)")
call()



