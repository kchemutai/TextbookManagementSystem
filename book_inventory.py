from book import Book
import logging
from binary_search_tree import BinarySearchTree
from threading import Lock

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class BookInventory:
    def __init__(self):
        self.books = {}
        self.cache = {}
        self.bst = BinarySearchTree()
        self.lock = Lock()

    def add_book(self, isbn, title, author, edition, category):
        with self.lock:
            if isbn in self.books:
                logging.warning(f"Book with ISBN {isbn} already exists.")
                return
            book = Book(isbn, title, author, edition, category)
            self.books[isbn] = book
            self.bst.insert(category, book)

    def retrieve_book(self, isbn):
        with self.lock:
            if isbn in self.cache:
                logging.info(f"Cache hit for ISBN: {isbn}")
                return self.cache[isbn]
            if isbn not in self.books:
                logging.error(f"Book with ISBN {isbn} not found.")
                raise KeyError(f"Book with ISBN {isbn} not found.")
            book = self.books[isbn]
            self.cache[isbn] = book
            return book

    def search_books(self, **kwargs):
        with self.lock:
            results = self.books.values()
            for attr, value in kwargs.items():
                results = filter(lambda book: getattr(book, attr, None) == value, results)
            return list(results)

    def update_availability(self, isbn, availability):
        with self.lock:
            if isbn not in self.books:
                logging.error(f"Cannot update availability: Book with ISBN {isbn} not found.")
                raise KeyError(f"Book with ISBN {isbn} not found.")
            self.books[isbn].availability = availability
