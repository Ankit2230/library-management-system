
import datetime

class Book:
    def __init__(self, title, author, isbn, total_copies,available_copies=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = available_copies if available_copies is not None else total_copies

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, total_copies={self.total_copies}, available_copies={self.available_copies})"


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"User(name={self.name}, user_id={self.user_id})"

class Checkout:
    def __init__(self, user_id, isbn, return_date=None):
        self.user_id = user_id
        self.isbn = isbn
        self.return_date = (return_date if return_date else (datetime.date.today() + datetime.timedelta(days=15))).strftime('%Y-%m-%d')

    def __repr__(self):
        return f"Checkout(user_id={self.user_id}, isbn={self.isbn}, return_date={self.return_date})"
