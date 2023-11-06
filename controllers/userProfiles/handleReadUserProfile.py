import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from userProfiles import UserProfile

class HandleReadUser:
    def __init__(self, database_file):
        self.database_file = database_file

    def read_user(self, user_id):
        user_account = UserProfile(self.database_file)
        user = user_account.read(user_id)
        user_account.close()
        return user