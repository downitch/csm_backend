import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from roles import Role

class HandleDeleteRole:
    def __init__(self, database_file):
        self.database_file = database_file

    def delete_role(self, role_id):
        role = Role(self.database_file)
        role.delete(role_id)
        role.close()