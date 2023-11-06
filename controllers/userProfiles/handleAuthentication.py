import sys
import os
import random
import string

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from userProfiles import UserProfile  # Replace with the actual import path

class HandleAuthentication:
    def __init__(self, database_file):
        print('auth module loaded')
        self.database_file = database_file

    def auth(self, email, password):
        # Use the UserProfile entity to check if the user exists with the given email and password
        user_account = UserProfile(self.database_file)
        users = user_account.search(email)
        user_account.close()

        if users:
            for user in users:
                if user["email"] == email and user["password"] == password:
                    # User with the provided email exists, generate a random alphanumeric token
                    token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                    return token
        return None  # User not found

    def unauth(self, token):
        print(f"{token} has been revoked.")
        # For simplicity, we just return True to indicate successful logout
        # In a real application, you might want to invalidate or delete the token
        return True
