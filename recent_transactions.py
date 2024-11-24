from collections import deque

class RecentTransactions:
    def __init__(self):
        self.transactions = deque()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_recent_transaction(self):
        if not self.transactions:
            return None
        return self.transactions.pop()
