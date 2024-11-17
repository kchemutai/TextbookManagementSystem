class BorrowHistoryNode:
    def __init__(self, user, borrow_date):
        self.user = user
        self.borrow_date = borrow_date
        self.return_date = None
        self.next = None