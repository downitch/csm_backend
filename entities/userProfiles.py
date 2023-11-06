import sqlite3

class UserProfile:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()

    def create(self, login, email, password, first_name, last_name, dob, role_id):
        self.cursor.execute("INSERT INTO user_accounts (login, email, password, first_name, last_name, DOB, role_id) VALUES (?, ?, ?, ?, ?, ?, ?)", (login, email, password, first_name, last_name, dob, role_id))
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, user_account_id):
        self.cursor.execute("SELECT * FROM user_accounts WHERE ID = ?", (user_account_id,))
        return self.cursor.fetchone()

    def update(self, user_account_id, login, email, password, first_name, last_name, dob, role_id):
        self.cursor.execute("UPDATE user_accounts SET login = ?, email = ?, password = ?, first_name = ?, last_name = ?, DOB = ?, role_id = ? WHERE ID = ?", (login, email, password, first_name, last_name, dob, role_id, user_account_id))
        self.conn.commit()

    def delete(self, user_account_id):
        self.cursor.execute("DELETE FROM user_accounts WHERE ID = ?", (user_account_id,))
        self.conn.commit()

    def search(self, email):
        self.cursor.execute("SELECT * FROM user_accounts WHERE email = ?", (email,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()