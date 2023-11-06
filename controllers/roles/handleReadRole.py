import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from roles import Role

class HandleReadRole:
    def __init__(self, database_file):
        self.database_file = database_file

    def read_role(self, role_id):
        role = Role(self.database_file)
        role_data = role.read(role_id)
        role.close()
        return role_data