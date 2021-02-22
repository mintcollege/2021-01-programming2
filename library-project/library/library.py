from datetime import datetime
from library.student import Student


class Book:
    def __init__(self, title: str, published: int = None):
        self.title = title
        self.published = published

    def __str__(self):
        return self.title


class Library:
    booklist = []
    borrowed = []
    is_open = False
    
    def __init__(self, name: str = 'Samantha'):
        self.name = name
        
    def addbook(self, book: Book):
        self.booklist.append(book)
        
    def get_booklist(self):
        titles = []
        for book in self.booklist:
            titles.append(book.title)
        return titles
    
    def borrow(self, book: Book, student: Student):
        if self.is_open:
            self.borrowed.append({
                'student': student,
                'book': book,
                'date_borrowed': datetime.now()
            })
        else:
            print('Library is not open at this time. Sorry.')
        
    def borrow_many(self, books: list, student: Student):
        if self.is_open:
            for book in books:
                self.borrow(book, student)
        else:
            print('Library is not open at this time. Sorry.')
            
            
    def return_book(self, book: Book):
        pass
    
    
    def donate_book(self, books: list):
        pass
    
    
    def destroy_book(self, book: Book):
        pass
    
    
    def ban_student(self, student: Student):
        pass
    
    
    def unban_student(self, student: Student):
        pass
    
    
    def open_library(self):
        self.is_open = True
    
    
    def close_library(self):
        self.is_open = False
        


