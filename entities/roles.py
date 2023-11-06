import sqlite3

class Role:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()

    def create(self, name, description):
        self.cursor.execute("INSERT INTO roles (name, description) VALUES (?, ?)", (name, description))
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, role_id):
        self.cursor.execute("SELECT * FROM roles WHERE ID = ?", (role_id,))
        return self.cursor.fetchone()

    def update(self, role_id, name, description):
        self.cursor.execute("UPDATE roles SET name = ?, description = ? WHERE ID = ?", (name, description, role_id))
        self.conn.commit()

    def delete(self, role_id):
        self.cursor.execute("DELETE FROM roles WHERE ID = ?", (role_id,))
        self.conn.commit()

    def search(self, name):
        self.cursor.execute("SELECT * FROM roles WHERE name = ?", (name,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()