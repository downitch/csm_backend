import sqlite3

class Timeslot:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()

    def create(self, frame, exact_date):
        self.cursor.execute("INSERT INTO timeslots (frame, exact_date) VALUES (?, ?)", (frame, exact_date))
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, timeslot_id):
        self.cursor.execute("SELECT * FROM timeslots WHERE ID = ?", (timeslot_id,))
        return self.cursor.fetchone()

    def update(self, timeslot_id, frame, exact_date):
        self.cursor.execute("UPDATE timeslots SET frame = ?, exact_date = ? WHERE ID = ?", (frame, exact_date, timeslot_id))
        self.conn.commit()

    def delete(self, timeslot_id):
        self.cursor.execute("DELETE FROM timeslots WHERE ID = ?", (timeslot_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()