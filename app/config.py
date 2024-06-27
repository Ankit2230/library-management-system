import os
import json

# Set BASE_DIR to the current working directory
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Define file paths relative to BASE_DIR
BOOKS_FILE = os.path.join(DATA_DIR, 'books.json')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
CHECKOUTS_FILE = os.path.join(DATA_DIR, 'checkouts.json')

print("BOOKS_FILE",BOOKS_FILE)
print("USERS_FILE",USERS_FILE)
print("CHECKOUTS_FILE",CHECKOUTS_FILE)
# Ensure the data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Ensure the JSON files exist
for file_path in [BOOKS_FILE, USERS_FILE, CHECKOUTS_FILE]:
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file, indent=4)
