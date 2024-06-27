from models import Book
from storage import BookStorage
from config import BOOKS_FILE

class BookManager:
    def __init__(self, storage_file=BOOKS_FILE):
        self.storage = BookStorage(storage_file)
        self.books = self.storage.load_books()

    def add_book(self, title, author, isbn, total_copies):
        existing_book = self.get_book_by_isbn(isbn)
        if existing_book:
            if existing_book.title == title and existing_book.author == author:
                existing_book.total_copies += total_copies
                existing_book.available_copies += total_copies
                self.storage.save_books(self.books)
                print(f"Added {total_copies} more copies of the book with ISBN {isbn}.")
            else:
                print(f"A different author ({existing_book.author}) is already associated with ISBN {isbn}.")
                print("Please check the ISBN")
            return

        book = Book(title, author, isbn, total_copies)
        self.books.append(book)
        self.storage.save_books(self.books)
        print("Book added.")

    def list_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book)

    def get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def book_exists(self, isbn):
        return any(book.isbn == isbn for book in self.books)

    def update_book(self, updated_book):
        for i, book in enumerate(self.books):
            if book.isbn == updated_book.isbn:
                self.books[i] = updated_book
                self.storage.save_books(self.books)
                print(f"Book with ISBN {updated_book.isbn} updated.")
                return True
        print(f"Book with ISBN {updated_book.isbn} not found.")
        return False

    def remove_book(self, isbn):
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]
                self.storage.save_books(self.books)
                print(f"Book with ISBN {isbn} removed.")
                return True
        print(f"Book with ISBN {isbn} not found.")
        return False
