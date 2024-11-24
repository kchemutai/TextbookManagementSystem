from linked_list import LinkedList

class Book:
    def __init__(self, isbn, title, author, edition, category, availability=True):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.edition = edition
        self.category = category
        self.availability = availability
        self.borrow_history = LinkedList()
