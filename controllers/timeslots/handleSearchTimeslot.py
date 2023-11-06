import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from timeslots import Timeslot

class HandleSearchTimeslot:
    def __init__(self, database_file):
        self.database_file = database_file

    def search_timeslot(self, frame):
        timeslot = Timeslot(self.database_file)
        timeslots = timeslot.search(frame)
        timeslot.close()
        return timeslots