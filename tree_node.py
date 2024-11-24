class TreeNode:
    def __init__(self, key, books=None):
        self.key = key
        self.books = books if books is not None else []  # Store a list of books for the same key
        self.left = None
        self.right = None