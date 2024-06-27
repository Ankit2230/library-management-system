import datetime
from models import Checkout
from storage import CheckoutStorage
from config import CHECKOUTS_FILE

class CheckoutManager:
    def __init__(self, book_manager, user_manager, storage_file=CHECKOUTS_FILE):
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.storage = CheckoutStorage(storage_file)
        self.checkouts = self.storage.load_checkouts()

    def checkout_book(self, user_id, isbn):
        if not self.user_manager.user_exists(user_id):
            print(f"User with ID {user_id} does not exist.")
            return False

        book = self.book_manager.get_book_by_isbn(isbn)
        if not book:
            print(f"Book with ISBN {isbn} does not exist.")
            return False

        if book.available_copies <= 0:
            print(f"No copies of the book with ISBN {isbn} are available for checkout.")
            return False

        checkout = Checkout(user_id, isbn, datetime.date.today() + datetime.timedelta(days=15))
        self.checkouts.append(checkout)
        book.available_copies -= 1
        self.book_manager.storage.save_books(self.book_manager.books)
        self.storage.save_checkouts(self.checkouts)
        print(f"Book with ISBN {isbn} checked out to user {user_id} until {checkout.return_date}.")
        return True

    def is_book_checked_out(self, isbn):
        book = self.book_manager.get_book_by_isbn(isbn)
        return book and book.available_copies < book.total_copies

    def list_checkouts(self):
        if not self.checkouts:
            print("No books checked out.")
        else:
            for checkout in self.checkouts:
                print(f"User ID: {checkout.user_id}, ISBN: {checkout.isbn}")
    
    def return_book(self, user_id, isbn):
        for checkout in self.checkouts:
            if checkout.user_id == user_id and checkout.isbn == isbn:
                return_date = datetime.datetime.strptime(checkout.return_date, '%Y-%m-%d').date()
                self.checkouts.remove(checkout)
                book = self.book_manager.get_book_by_isbn(isbn)
                if book:
                    book.available_copies += 1
                    self.book_manager.storage.save_books(self.book_manager.books)
                self.storage.save_checkouts(self.checkouts)
                if return_date >= datetime.date.today():
                    print(f"Book with ISBN {isbn} returned on time.")
                else:
                    print(f"Book with ISBN {isbn} returned late.")
                return True
        print("No such checkout found.")
        return False

