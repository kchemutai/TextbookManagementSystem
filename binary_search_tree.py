from tree_node import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, book):
        if self.root is None:
            self.root = TreeNode(key, [book])
        else:
            self._insert(self.root, key, book)

    def _insert(self, node, key, book):
        if key == node.key:
            node.books.append(book)  # Add the book to the existing key's list
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key, [book])
            else:
                self._insert(node.left, key, book)
        else:  # key > node.key
            if node.right is None:
                node.right = TreeNode(key, [book])
            else:
                self._insert(node.right, key, book)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.books
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
