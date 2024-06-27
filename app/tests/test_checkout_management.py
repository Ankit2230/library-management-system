import unittest
from book_management import BookManager
from user_management import UserManager
from checkout_management import CheckoutManager
from models import Book, User

class TestCheckoutManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager('data/test_books.json')
        self.user_manager = UserManager('data/test_users.json')
        self.checkout_manager = CheckoutManager(self.book_manager, self.user_manager, 'data/test_checkouts.json')

    def tearDown(self):
        import os
        os.remove('data/test_books.json')
        os.remove('data/test_users.json')
        os.remove('data/test_checkouts.json')

    def test_checkout_book(self):
        self.book_manager.add_book('Test Book', 'Test Author', '1234567890',1)
        self.user_manager.add_user('Test User', '1')
        result = self.checkout_manager.checkout_book('1', '1234567890')
        self.assertTrue(result)
        self.assertTrue(self.checkout_manager.is_book_checked_out('1234567890'))

    def test_return_book(self):
        self.book_manager.add_book('Test Book', 'Test Author', '1234567890',1)
        self.user_manager.add_user('Test User', '1')
        self.checkout_manager.checkout_book('1', '1234567890')
        result = self.checkout_manager.return_book('1', '1234567890')
        self.assertTrue(result)
        self.assertFalse(self.checkout_manager.is_book_checked_out('1234567890'))

if __name__ == '__main__':
    unittest.main()
