import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from timeslots import Timeslot

class HandleReadTimeslot:
    def __init__(self, database_file):
        self.database_file = database_file

    def read_timeslot(self, timeslot_id):
        timeslot = Timeslot(self.database_file)
        timeslot_data = timeslot.read(timeslot_id)
        timeslot.close()
        return timeslot_data