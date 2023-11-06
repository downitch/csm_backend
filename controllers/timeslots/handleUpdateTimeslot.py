import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from timeslots import Timeslot

class HandleUpdateTimeslot:
    def __init__(self, database_file):
        self.database_file = database_file

    def update_timeslot(self, timeslot_id, frame, exact_date):
        timeslot = Timeslot(self.database_file)
        timeslot.update(timeslot_id, frame, exact_date)
        timeslot.close()