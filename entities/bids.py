import sqlite3

class Bid:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()

    def create(self, timeslot_id, user_account_id, reviewed, approved):
        self.cursor.execute("INSERT INTO bids (timeslot_id, user_account_id, reviewed, approved) VALUES (?, ?, ?, ?)", (timeslot_id, user_account_id, reviewed, approved))
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, bid_id):
        self.cursor.execute("SELECT * FROM bids WHERE ID = ?", (bid_id,))
        return self.cursor.fetchone()

    def update(self, bid_id, timeslot_id, user_account_id, reviewed, approved):
        self.cursor.execute("UPDATE bids SET timeslot_id = ?, user_account_id = ?, reviewed = ?, approved = ? WHERE ID = ?", (timeslot_id, user_account_id, reviewed, approved, bid_id))
        self.conn.commit()

    def delete(self, bid_id):
        self.cursor.execute("DELETE FROM bids WHERE ID = ?", (bid_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
