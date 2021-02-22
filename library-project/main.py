from library.library import Library, Book
from library.student import Student
from icecream import ic

# Object creation
lib = Library('MINT Library')
lotr1 = Book('Fellowship of the Ring', 1955)
lotr2 = Book('Twin Towers', 1965)
lotr3 = Book('Return of the King', 1975)
domes = Book('Domes of Fire', 1990)
mark = Student(4527, 'Mark Santos')
shawn = Student(7533, 'Shawn Mendez')

lib.addbook(lotr1)
lib.addbook(lotr2)
lib.addbook(lotr3)

lib.open_library()
lib.borrow_many([lotr1, lotr2, lotr3], mark)
lib.borrow(domes, shawn)
lib.close_library()
ic(lib.borrowed)


if __name__ == '__main__':
    pass