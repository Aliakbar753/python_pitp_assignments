class Book:
    title = ""
    auther = ""
    pages = 0

    def book_details(self,title,auther,pages):
        self.title = title
        self.auther = auther
        self.pages = pages
        print(f"book is {self.title}, auther is {self.auther}, pages are {self.pages}")

book = Book()

title1 = input("Enter book title : ")
auther1 = input("Enter book auther: ")
pages1 = int(input("enter book pages : "))

book.book_details(title1, auther1, pages1)