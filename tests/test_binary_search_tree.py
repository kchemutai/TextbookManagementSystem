import unittest
from binary_search_tree import BinarySearchTree
from book import Book

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert_and_search(self):
        book = Book("12345", "Python Programming", "John Doe", "1st", "Technology")
        self.bst.insert("Technology", book)
        result = self.bst.search("Technology")
        
        # Verify the result is a list containing the correct book
        self.assertIsInstance(result, list)  # Ensure result is a list
        self.assertEqual(len(result), 1)  # Ensure only one book is present
        self.assertEqual(result[0].title, "Python Programming")  # Validate the book's title

    def test_insert_duplicate_keys(self):
        book1 = Book("12345", "Python Programming", "John Doe", "1st", "Technology")
        book2 = Book("67890", "Advanced Python", "Jane Smith", "2nd", "Technology")
        self.bst.insert("Technology", book1)
        self.bst.insert("Technology", book2)
        result = self.bst.search("Technology")
        
        # Verify both books are present under the same key
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].title, "Python Programming")
        self.assertEqual(result[1].title, "Advanced Python")

if __name__ == "__main__":
    unittest.main()
