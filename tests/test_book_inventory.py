import unittest
from book_inventory import BookInventory

class TestBookInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = BookInventory()

    def test_add_book(self):
        self.inventory.add_book("12345", "Python Programming", "John Doe", "1st", "Technology")
        book = self.inventory.retrieve_book("12345")
        self.assertEqual(book.title, "Python Programming")

    def test_update_availability(self):
        self.inventory.add_book("12345", "Python Programming", "John Doe", "1st", "Technology")
        self.inventory.update_availability("12345", False)
        book = self.inventory.retrieve_book("12345")
        self.assertFalse(book.availability)

    def test_search_books(self):
        self.inventory.add_book("12345", "Python Programming", "John Doe", "1st", "Technology")
        results = self.inventory.search_books(category="Technology")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Python Programming")

if __name__ == "__main__":
    unittest.main()
