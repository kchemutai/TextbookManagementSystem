from book import Book
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

book_inventory = {}

def add_book(isbn, title, author, edition, category):
    book = Book(isbn, title, author, edition, category, True)
    book_inventory[isbn] = book

def retrieve_book(isbn):
    if isbn not in book_inventory:
        logging.error(f"Book with ISBN {isbn} not found in the inventory.")
        raise KeyError(f"Book with ISBN {isbn} not found in the inventory.")
    return book_inventory[isbn]

def update_availability(isbn, availability):
    if isbn not in book_inventory:
        logging.error(f"Cannot update availability: Book with ISBN {isbn} not found.")
        raise KeyError(f"Cannot update availability: Book with ISBN {isbn} not found.")
    book_inventory[isbn].availability = availability
