class LibraryItem:
    def __init__(self,name,title,pages):
        self.name = name 
        self.title = title
        self.pages = pages

    def __eq__(self,other):
        return (self.title == other.title)
    
    def __str__(self):
        return f"Name: {self.name} | Title: {self.title}"
    
    def __len__(self):
        return self.pages
    
class Book(LibraryItem):
    def __init__(self,name,title,quantity,pages):
        super().__init__(name,title,pages)
        self.quantity = quantity


class Magazine(LibraryItem):
    def __init__(self,name,title,author,pages):
        super().__init__(name,title,pages)
        self.author = author

Book1 =  Book("India today","Femina India",2,58)
Magazine1 = Magazine("Womens","Meri","Chetan Bhagat",99)
Book2 = Book("Fashion", "GQ India",3,99)
print(Book1)
print(Magazine1)
print(Book2)
print("Are book and magazine are of same title?",Book1 == Magazine1)
print("Some details about book and magazine is:",Book1,Magazine1)
print("Length of book1 is:",len(Book1))
