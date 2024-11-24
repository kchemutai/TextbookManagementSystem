import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("12345", "Python Programming", "John Doe", "1st", "Technology")
        self.assertEqual(book.isbn, "12345")
        self.assertEqual(book.title, "Python Programming")
        self.assertTrue(book.availability)

if __name__ == "__main__":
    unittest.main()
