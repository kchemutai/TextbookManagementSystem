recent_transactions = []

def add_transaction(transaction):
    recent_transactions.append(transaction)

def get_recent_transaction():
    return recent_transactions.pop() if recent_transactions else None
