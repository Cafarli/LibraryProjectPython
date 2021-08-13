class Book:
    def __init__(self,id,name,desc,isbn,pages,author,issued,year):
        self.id=id
        self.name=name
        self.desc=desc
        self.isbn=isbn
        self.pages=pages
        self.author=author
        self.issued=issued
        self.year=year
    
    

    def to_dict(self):
        dictionary={
            "id":self.id,
            "name":self.name,
            "desc":self.desc,
            "isbn":self.isbn,
            "pages":self.pages,
            "author":self.author,
            "issued":self.issued,
            "year":self.year
        }
        return dictionary
