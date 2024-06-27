import unittest
from book_management import BookManager
from models import Book

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager('data/test_books.json')

    def tearDown(self):
        import os
        os.remove('data/test_books.json')

    def test_add_book(self):
        self.book_manager.add_book('Test Book', 'Test Author', '1234567890',1)
        book = self.book_manager.get_book_by_isbn('1234567890')
        self.assertIsNotNone(book)
        self.assertEqual(book.title, 'Test Book')

    def test_list_books(self):
        self.book_manager.add_book('Test Book', 'Test Author', '1234567890',1)
        self.book_manager.add_book('Another Book', 'Another Author', '0987654321',1)
        books = self.book_manager.books
        self.assertEqual(len(books), 2)

    def test_remove_book(self):
        self.book_manager.add_book('Test Book', 'Test Author', '1234567890',1)
        self.book_manager.remove_book('1234567890')
        book = self.book_manager.get_book_by_isbn('1234567890')
        self.assertIsNone(book)

if __name__ == '__main__':
    unittest.main()
