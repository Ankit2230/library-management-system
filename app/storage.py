import json
import os
import datetime
from models import Book, User, Checkout

from config import BOOKS_FILE,CHECKOUTS_FILE,USERS_FILE
class StorageManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_data(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

class BookStorage(StorageManager):
    def __init__(self, file_name=BOOKS_FILE):
        super().__init__(file_name)

    def save_books(self, books):
        self.save_data([book.__dict__ for book in books])

    def load_books(self):
        data = self.load_data()
        return [Book(**item) for item in data]

class UserStorage(StorageManager):
    def __init__(self, file_name=USERS_FILE):
        super().__init__(file_name)

    def save_users(self, users):
        self.save_data([user.__dict__ for user in users])

    def load_users(self):
        data = self.load_data()
        return [User(**item) for item in data]

class CheckoutStorage(StorageManager):
    def __init__(self, file_name=CHECKOUTS_FILE):
        super().__init__(file_name)

    def save_checkouts(self, checkouts):
        self.save_data([checkout.__dict__ for checkout in checkouts])

    def load_checkouts(self):
        data = self.load_data()
        # Convert string back to date
        return [Checkout(**{**item, 'return_date': datetime.datetime.strptime(item['return_date'], '%Y-%m-%d').date()}) for item in data]
