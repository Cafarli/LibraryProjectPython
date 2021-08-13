import BookOperations 
import os 

def options():
    print("1- create a new book")
    print("2- save books locally")
    print("3- load books from the disk")
    print("4- issue a book")
    print("5- return a book")
    print("6- update a book")
    print("7- show all books")
    print("8- show a book")

options()
option=input("Choose action number: ")

books = []
while option.lower() !='x':
    if option=='1':
        books.append(BookOperations.createnewbook())
    elif option=='2':
        BookOperations.save_book_locally(books)
    elif option=='3': 
        books = BookOperations.load_book()
    elif option=='4':
        print(BookOperations.issue_book(books))
    elif option=='5':
        BookOperations.return_book(books)
    elif option=='6':
        BookOperations.update_book(books)
    elif option=='7':
        BookOperations.show_all_book(books)
    elif option=='8':
        BookOperations.show_book(books)
    else:
        print("The given command doesn't exist...")
    input("command executed ... press any button to continue")
    os.system('cls')
    options()
    option=input("Choose action number: ")
