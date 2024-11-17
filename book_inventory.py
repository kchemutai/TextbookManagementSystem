from book import Book

book_inventory = {}

def add_book(isbn, title, author, edition, category):
    book = Book(isbn, title, author, edition, category, True)
    book_inventory[isbn] = book

def retrieve_book(isbn):
    return book_inventory.get(isbn)

def update_availability(isbn, availability):
    if isbn in book_inventory:
        book_inventory[isbn].availability = availability
