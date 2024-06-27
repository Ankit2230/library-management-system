from models import User
from storage import UserStorage
from config import USERS_FILE

class UserManager:
    def __init__(self, storage_file=USERS_FILE):
        self.storage = UserStorage(storage_file)
        self.users = self.storage.load_users()

    def add_user(self, name, user_id):
        if self.user_exists(user_id):
            print(f"User with ID {user_id} already exists.")
            return False
        user = User(name, user_id)
        self.users.append(user)
        self.storage.save_users(self.users)
        print(f"User {name} with ID {user_id} added.")
        return True

    def user_exists(self, user_id):
        return any(user.user_id == user_id for user in self.users)

    def list_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            print(user)
