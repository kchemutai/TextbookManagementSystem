from borrow_history import BorrowHistoryNode

class LinkedList:
    def __init__(self):
        self.head = None

    def add_borrow_record(self, user, borrow_date):
        new_record = BorrowHistoryNode(user, borrow_date)
        new_record.next = self.head
        self.head = new_record

    def update_return_record(self, user, return_date):
        current = self.head
        while current:
            if current.user == user and current.return_date is None:
                current.return_date = return_date
                break
            current = current.next
            