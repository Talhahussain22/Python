class Library:
    def __init__(self):
        self.number_of_books=0
        self.books=[]

    def add(self,book):
        self.number_of_books+=1
        self.books.append(book)

    def show_books(self):
        print(f"The libarary has {self.number_of_books} books and are:")
        for i in self.books:
            print(i)

    def check_validity(self):
        if self.number_of_books==len(self.books):
            print("Both are equal")

book1=Library()
book1.add("Physics")
book1.add("Chemistry")
book1.show_books()
book1.check_validity()




