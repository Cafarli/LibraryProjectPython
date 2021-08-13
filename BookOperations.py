from book import Book
import json
import sys 

def input_book_info():
    print("Write your book information")
    id=input("ID:")
    name=input("Name:")
    desc=input("Description:")
    isbn=int(input("ISBN:"))
    pages=int(input("Pages:"))
    author=input("Author:")
    issued=input("Issued(true or false):")
    year=int(input("Year:"))
    return {
        'id' : id,
        'name' : name,
        'desc' : desc,
        'isbn' : isbn,
        'pages' : pages,
        'author' : author,
        'issued' : issued,
        'year' : year
    }

def createnewbook():
    book_input = input_book_info()
    book = Book(book_input['id'],book_input['name'],book_input['desc'],
    book_input['isbn'],book_input['pages'],book_input['author'],book_input['issued'],book_input['year'])
    print(book.to_dict())
    return book
    
def save_book_locally(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    try:
        file = open("books.dat","w")
        file.write(json.dumps(json_books,indent=4))
    except:
        print("Error")
    pass
def load_book():
    try:
        file = open("books.dat","r")
        loaded_books = json.loads(file.read())
        books =[]
        for book in loaded_books:
            newobj = Book(book['id'],book['name'],book['desc'],book['isbn'],book['pages'],book['author'],
            book['issued'],book['year'])
            books.append(newobj)
        print("Succesfully loaded books")
        return books
    except Exception:
        print("The file doesn't exist or an error occured during loading\n")
def find_book(books, id):
    for index, book in enumerate(books):
        if book.id == id:
            return index
        return None 

def issue_book(books):
    id = input("Enter the id of the book you want to issue: ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = True
        print("Book succesfully updated.")
    else:
        print("System can't fond the book you are looking for.")

def return_book(books):
    id = input("Enter the id of the book you want to return: ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = False
        print("Book succesfully returned.")
    else:
        print("System can't fond the book you are looking for.")
def update_book(books):
    id = input("Enter the ID of the book you want to update: ")
    index = find_book(books, id)
    if index != None:
        new_book = createnewbook()
        old_book = books[index]
        books[index] = new_book
        del old_book
        print("Book succesfully updated.")
    else:
        print("System can't fond the book you are looking for.")
def show_all_book(books):
    for book in books:
        print(book.to_dict())

def show_book(books):
    id = input("Enter the ID of the book you want to update: ")
    index = find_book(books, id)
    if index != None:
        print(books[index].to_dict())
    else:
        print("System can't fond the book you are looking for.")
