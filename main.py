from book_inventory import add_book, retrieve_book, update_availability
from recent_transactions import add_transaction, get_recent_transaction
import recent_transactions
from transaction import Transaction

# Adding books
add_book("12345", "Python Programming", "John Doe", "1st", "Technology")
add_book("67890", "Data Structures", "Jane Smith", "2nd", "Computer Science")

# Retrieving and updating a book
book = retrieve_book("12345")
print(f"Retrieved: {book.title}, Available: {book.availability}")

# Borrow a book
update_availability("12345", False)
book.borrow_history.add_borrow_record("Alice", "2024-11-17")
add_transaction(Transaction("12345", "Alice", "borrow", "2024-11-17"))

# Return a book
book.borrow_history.update_return_record("Alice", "2024-11-20")
update_availability("12345", True)
add_transaction(Transaction("12345", "Alice", "return", "2024-11-20"))

# View recent transactions
while True:
    transaction = get_recent_transaction()
    if transaction is None:
        break
    print(f"Transaction: {transaction.action} {transaction.isbn} by {transaction.user} on {transaction.date}")

