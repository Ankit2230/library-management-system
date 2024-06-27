# Library Management System

This project implements a command-line Library Management System (LMS) using Python. The system allows users to manage books and users, perform checkouts, and manage returns, including handling late returns. Below, you'll find an overview of the system architecture, class structure, and usage instructions.

## System Architecture

The Library Management System is structured around three main components:

1. **Book Management**: Handles operations related to books, such as adding new books, listing all books, verifying book existence, updating books, and removing books.
2. **User Management**: Manages users, including adding new users, retrieving users by ID, and verifying user existence.
3. **Checkout Management**: Facilitates checking out books to users, tracking current checkouts, managing book returns, and handling late returns.

The system is designed to be modular and scalable, allowing for easy extension with new features or modifications to existing functionalities.

## Class Structure

### `BookManager` Class

Responsible for managing operations related to books:

- **Attributes**:
  - `books`: List of `Book` objects representing the library's collection.
  - `storage`: Instance of `BookStorage` for handling data persistence.

- **Methods**:
  - `add_book(title, author, isbn)`: Adds a new book to the collection.
  - `list_books()`: Lists all books currently in the library.
  - `get_book_by_isbn(isbn)`: Retrieves a book object by its ISBN.
  - `book_exists(isbn)`: Checks if a book with a given ISBN exists in the collection.
  - `update_book(updated_book)`: Updates an existing book with new details.
  - `remove_book(isbn)`: Removes a book from the collection.

### `UserManager` Class

Handles user-related operations:

- **Attributes**:
  - `users`: List of `User` objects representing library users.
  - `storage`: Instance of `UserStorage` for data storage and retrieval.

- **Methods**:
  - `add_user(name, user_id)`: Adds a new user to the system. Checks for existing user ID to prevent duplicates and appends new users to the list if not already present.
  - `user_exists(user_id)`: Checks if a user with a given ID exists in the system, ensuring that operations like adding a new user are only performed if the user ID does not already exist.
  - `list_users()`: Displays all users currently registered in the system. If no users are found, it prints a message indicating that no users are available.


### `CheckoutManager` Class

Manages book checkout and return operations:

- **Attributes**:
  - `book_manager`: Instance of `BookManager` for book-related operations.
  - `user_manager`: Instance of `UserManager` for user-related operations.
  - `storage`: Instance of `CheckoutStorage` for managing checkout data.
  - `checkouts`: List of `Checkout` objects representing current book checkouts.

- **Methods**:
  - `checkout_book(user_id, isbn)`: Checks out a book to a user, setting a return date.
  - `is_book_checked_out(isbn)`: Checks if a book with a given ISBN is currently checked out.
  - `list_checkouts()`: Lists all currently checked out books.
  - `return_book(user_id, isbn)`: Handles the return of checked-out books, checking for timeliness.

## Usage

1. **Setup**:
   - Ensure Python 3.x is installed on your system.
   - Clone the repository: `git clone https://github.com/your/repo.git`
   - Navigate to the project directory: `cd library-management-system`

2. **Installation**:
   - Install dependencies (if any): `pip install -r requirements.txt`

3. **Running the Application**:
  - Navigate to the app folder: cd app
  - Run the main script: `python3 main.py / python main.py`
  - Follow the on-screen prompts to perform operations such as adding books, adding users, listing books, checking out books, and managing returns.

4. **Additional Notes**:
   - Ensure that the `data` directory exists and is writable for storing JSON data files (`books.json`, `users.json`, `checkouts.json`).

## Design Decisions

- **Object-Oriented Approach**: Utilized classes (`Book`, `User`, `Checkout`, `BookManager`, `UserManager`, `CheckoutManager`) to encapsulate related functionalities and ensure clear separation of concerns.
- **Modularity**: Each component (book management, user management, checkout management) is encapsulated in its own module (`book_management.py`, `user_management.py`, `checkout_management.py`), promoting code reusability and maintainability.
- **Data Persistence**: Implemented file-based storage using JSON files (`books.json`, `users.json`, `checkouts.json`) and utilized respective `Storage` classes (`BookStorage`, `UserStorage`, `CheckoutStorage`) for data loading and saving operations.
- **Error Handling**: Incorporated basic error handling to manage exceptions and validate user inputs, ensuring robustness and reliability of the system.
