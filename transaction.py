class Transaction:
    def __init__(self, isbn, user, action, date):
        self.isbn = isbn
        self.user = user
        self.action = action  # 'borrow' or 'return'
        self.date = date
