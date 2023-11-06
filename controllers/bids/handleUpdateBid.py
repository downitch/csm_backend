import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from bids import Bid

class HandleUpdateBid:
    def __init__(self, database_file):
        self.database_file = database_file

    def update_bid(self, bid_id, timeslot_id, user_account_id, reviewed, approved):
        bid = Bid(self.database_file)
        bid.update(bid_id, timeslot_id, user_account_id, reviewed, approved)
        bid.close()