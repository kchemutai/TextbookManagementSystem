import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_add_borrow_record(self):
        history = LinkedList()
        history.add_borrow_record("Alice", "2024-11-17")
        self.assertEqual(history.head.user, "Alice")
        self.assertEqual(history.head.borrow_date, "2024-11-17")

    def test_update_return_record(self):
        history = LinkedList()
        history.add_borrow_record("Alice", "2024-11-17")
        history.update_return_record("Alice", "2024-11-20")
        self.assertEqual(history.head.return_date, "2024-11-20")

if __name__ == "__main__":
    unittest.main()
