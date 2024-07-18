class Book:
    def __init__(self, title, category):
        self.title = title
        self.category = category
    
    def __str__(self):
        return f"Book, {self.title}, {self.category}"
    
class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError(f"{book} is not of type Book")
        
    def __getitem__(self, idx):
        return self.books[idx]
    
b1 = Book("python", "textbook")
b2 = Book("c++", "textbook")
b3 = Book("Blue moon", "novel")
b4 = Book("Pride and prejudice", "novel")

lib = Library()
lib.add(b1)
lib.add(b2)
lib.add(b3)
lib.add(b4)

print(lib[1])
for book in lib:
    print(book)