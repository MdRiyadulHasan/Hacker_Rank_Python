class Book:
    def __init__(self, title, quantity, author, price):
        self.title=title
        self.quantity = quantity
        self.author = author
        self.price = price
    
    def __repr__(self):
        #return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"
        return f'Book :{self.title}, Quantity : {self.quantity}, Author : {self.author}, price : {self.price}'
    

book1=Book('book1',20,'Hasan',150)
book2=Book('book2',30,'kamal',160)
book3=Book('book3',20,'Fahim',130)

print(book1)
print(book2)
print(book3)



