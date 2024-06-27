from book_management import BookManager
from user_management import UserManager
from checkout_management import CheckoutManager

class LibrarySystem:
    def __init__(self):
        self.book_manager = BookManager()
        self.user_manager = UserManager()
        self.checkout_manager = CheckoutManager(self.book_manager, self.user_manager)

    def main_menu(self):
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. Checkout Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Enter choice: ").strip()
        return choice

    def run(self):
        while True:
            choice = self.main_menu()
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.list_books()
            elif choice == '3':
                self.add_user()
            elif choice == '4':
                self.checkout_book()
            elif choice == '5':
                self.return_book()
            elif choice == '6':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")

    def add_book(self):
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        total_copies = int(input("Enter total copies: ").strip())
        if title and author and isbn and total_copies > 0:
            self.book_manager.add_book(title, author, isbn, total_copies)
        else:
            print("All fields are required. Book not added.")

    def list_books(self):
        self.book_manager.list_books()

    def add_user(self):
        name = input("Enter user name: ").strip()
        user_id = input("Enter user ID: ").strip()
        if name and user_id:
            self.user_manager.add_user(name, user_id)
        else:
            print("All fields are required. User not added.")

    def checkout_book(self):
        user_id = input("Enter user ID: ").strip()
        isbn = input("Enter ISBN of the book to checkout: ").strip()
        if not user_id or not isbn:
            print("All fields are required. Checkout not processed.")
            return
        
        if not self.user_manager.user_exists(user_id):
            print(f"User with ID {user_id} does not exist.")
            return
        
        if not self.book_manager.book_exists(isbn):
            print(f"Book with ISBN {isbn} does not exist.")
            return
        
        if not self.checkout_manager.checkout_book(user_id, isbn):
            print("Checkout failed. Check user ID and book ISBN.")
    
    def return_book(self):
        user_id = input("Enter user ID: ").strip()
        isbn = input("Enter ISBN of the book to return: ").strip()
        if not user_id or not isbn:
            print("All fields are required. Return process not completed.")
            return

        if self.checkout_manager.return_book(user_id, isbn):
            print("Book returned.")
        else:
            print("Failed to return book. Please check the details.")

if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.run()
