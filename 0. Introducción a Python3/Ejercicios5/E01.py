"""
Create two classes, Book and Author, that are related.
The Book class should have an author attribute, which is an instance of the Author class, as well as title and price attributes.
The author will have name and nationality attributes.
Print the title attribute.
"""

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

def main():
    author = Author("Cervantes", "Spanish")
    book = Book("Don Quixote", author, 30.99)

    print("The book ", book.title, " was written by ", book.author.name, " of nationality ", book.author.nationality)
    print("The price of the book is €", book.price)

if __name__ == "__main__":
    main()  