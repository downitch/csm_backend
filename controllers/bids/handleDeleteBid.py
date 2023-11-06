import sys
import os

# Add the path to the 'entities' directory to sys.path
current_dir = os.path.dirname(os.path.realpath(__file__))
entities_dir = os.path.join(current_dir, '../..', 'entities')
sys.path.append(entities_dir)

from bids import Bid

class HandleDeleteBid:
    def __init__(self, database_file):
        self.database_file = database_file

    def delete_bid(self, bid_id):
        bid = Bid(self.database_file)
        bid.delete(bid_id)
        bid.close()