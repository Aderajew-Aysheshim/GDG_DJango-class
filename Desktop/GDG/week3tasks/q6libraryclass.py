class Library:
  def __init__(self):
    self.books=[]
    
  def add_book(self,title):
    self.books.append(title)
  def show_books(self):
    print("Books in Library:")
    for book in self.books:
      print("-",book)
library=Library()
library.add_book("1984 by George Orwell")
library.add_book("To Kill a Mockingbird by Harper Lee")
library.show_books()
