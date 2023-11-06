import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from timeslots import Timeslot

class HandleDeleteTimeslot:
    def __init__(self, database_file):
        self.database_file = database_file

    def delete_timeslot(self, timeslot_id):
        timeslot = Timeslot(self.database_file)
        timeslot.delete(timeslot_id)
        timeslot.close()