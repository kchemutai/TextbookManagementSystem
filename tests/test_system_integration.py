import unittest
from book_inventory import BookInventory
from recent_transactions import RecentTransactions
from transaction import Transaction

class TestSystemIntegration(unittest.TestCase):
    def setUp(self):
        self.inventory = BookInventory()
        self.transactions = RecentTransactions()

    def test_full_workflow(self):
        # Add book
        self.inventory.add_book("12345", "Python Programming", "John Doe", "1st", "Technology")
        book = self.inventory.retrieve_book("12345")
        self.assertEqual(book.title, "Python Programming")

        # Borrow book
        book.borrow_history.add_borrow_record("Alice", "2024-11-17")
        self.transactions.add_transaction(Transaction("12345", "Alice", "borrow", "2024-11-17"))
        self.inventory.update_availability("12345", False)
        self.assertFalse(book.availability)

        # Return book
        book.borrow_history.update_return_record("Alice", "2024-11-20")
        self.transactions.add_transaction(Transaction("12345", "Alice", "return", "2024-11-20"))
        self.inventory.update_availability("12345", True)
        self.assertTrue(book.availability)

    def test_stress_test(self):
        # Add a large number of books
        for i in range(1000):
            isbn = f"ISBN{i:04d}"
            self.inventory.add_book(isbn, f"Book {i}", "Author", "1st", "General")
        self.assertEqual(len(self.inventory.books), 1000)

        # Search books
        results = self.inventory.search_books(category="General")
        self.assertEqual(len(results), 1000)

if __name__ == "__main__":
    unittest.main()
