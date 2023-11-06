import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from bids import Bid

class HandleSearchBid:
    def __init__(self, database_file):
        self.database_file = database_file

    def search_bid(self, timeslot_id, user_account_id):
        bid = Bid(self.database_file)
        bids = bid.search(timeslot_id, user_account_id)
        bid.close()
        return bids