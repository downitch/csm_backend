import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from roles import Role

class HandleCreateRole:
    def __init__(self, database_file):
        self.database_file = database_file

    def create_role(self, name, description):
        role = Role(self.database_file)
        role_id = role.create(name, description)
        role.close()
        return role_id