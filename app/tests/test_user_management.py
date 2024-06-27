import unittest
from user_management import UserManager
from models import User

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager('data/test_users.json')

    def tearDown(self):
        import os
        os.remove('data/test_users.json')

    def test_add_user(self):
        result = self.user_manager.add_user('Test User', '1')
        self.assertTrue(result)
        user = self.user_manager.user_exists('1')
        self.assertTrue(user)

    def test_list_users(self):
        self.user_manager.add_user('Test User', '1')
        self.user_manager.add_user('Another User', '2')
        users = self.user_manager.users
        self.assertEqual(len(users), 2)

if __name__ == '__main__':
    unittest.main()
