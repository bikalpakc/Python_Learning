class Library:
    def __init__(self):
        self.no_of_books=0
        self.books_list=[]

    def book_entry(self, book_name):
        self.books_list.append(book_name)
        self.no_of_books=len(self.books_list)  

    def show_details(self):
        print("The books available are:", self.books_list)
        print("The total number of books is:", self.no_of_books)     

obj1=Library()
book_name=input("Enter the Book you want to enter")   
obj1.book_entry(book_name)
obj1.show_details()
book_name=input("Enter the Second Book you want to enter") 
obj1.book_entry(book_name)
obj1.show_details()



