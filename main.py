from book_inventory import add_book, retrieve_book, update_availability
from recent_transactions import add_transaction, get_recent_transaction
from transaction import Transaction

# Adding books
add_book("12345", "Python Programming", "John Doe", "1st", "Technology")
add_book("67890", "Data Structures", "Jane Smith", "2nd", "Computer Science")

# Error handling demonstration
try:
    # Retrieving a book
    book = retrieve_book("12345")
    print(f"Retrieved: {book.title}, Available: {book.availability}")
except KeyError as e:
    print(e)

try:
    # Update availability for an existing book
    update_availability("12345", False)
    print(f"Updated availability for ISBN 12345.")
except KeyError as e:
    print(e)

try:
    # Update availability for a non-existent book
    update_availability("99999", False)
except KeyError as e:
    print(e)

# Borrow a book
book = retrieve_book("12345")
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
