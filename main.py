from book_inventory import BookInventory
from recent_transactions import RecentTransactions
from transaction import Transaction
from threading import Thread
from timeit import default_timer as timer

# Initialize systems
inventory = BookInventory()
transactions = RecentTransactions()

# Add sample books
inventory.add_book("12345", "Python Programming", "John Doe", "1st", "Technology")
inventory.add_book("67890", "Data Structures", "Jane Smith", "2nd", "Computer Science")

# Test retrieving and updating availability
print("Retrieving and updating availability for books:")
try:
    book = inventory.retrieve_book("12345")
    print(f"Retrieved: {book.title}, Available: {book.availability}")
    inventory.update_availability("12345", False)
    print(f"Availability updated for ISBN 12345: {book.availability}")
except KeyError as e:
    print(e)

# Borrowing and returning books
print("\nSimulating borrowing and returning books:")
book.borrow_history.add_borrow_record("Alice", "2024-11-17")
transactions.add_transaction(Transaction("12345", "Alice", "borrow", "2024-11-17"))
inventory.update_availability("12345", False)
print(f"Book borrowed: {book.title} by Alice on 2024-11-17")

book.borrow_history.update_return_record("Alice", "2024-11-20")
transactions.add_transaction(Transaction("12345", "Alice", "return", "2024-11-20"))
inventory.update_availability("12345", True)
print(f"Book returned: {book.title} by Alice on 2024-11-20")

# Advanced search functionality
print("\nAdvanced search functionality:")
inventory.add_book("11111", "AI Revolution", "Alice Tech", "3rd", "Technology")
tech_books = inventory.search_books(category="Technology")
print(f"Books in Technology category: {[book.title for book in tech_books]}")

# Stress testing: Adding 10,000 books
print("\nStress testing: Adding 10,000 books...")
def add_books(start, end):
    for i in range(start, end):
        inventory.add_book(f"ISBN{i:05d}", f"Book {i}", "Author {i}", "1st", "General")

t1 = Thread(target=add_books, args=(1, 5001))
t2 = Thread(target=add_books, args=(5001, 10001))
t1.start()
t2.start()
t1.join()
t2.join()
print("Concurrent addition of 10,000 books completed successfully.")

# Measuring performance of advanced search on a large dataset
print("\nMeasuring performance of advanced search:")
start = timer()
general_books = inventory.search_books(category="General")
end = timer()
print(f"Advanced search completed in {end - start:.4f} seconds.")
print(f"Total books in 'General' category: {len(general_books)}")

# Viewing recent transactions
print("\nViewing recent transactions:")
while True:
    transaction = transactions.get_recent_transaction()
    if not transaction:
        break
    print(f"Transaction: {transaction.action} ISBN: {transaction.isbn} by {transaction.user} on {transaction.date}")

print("\nAll tests completed successfully.")
