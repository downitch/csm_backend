import sqlite3
import os

# Check if the database file already exists
database_file = "sms.db"  # Change to your preferred database name
if not os.path.exists(database_file):
    # Create a new database if it doesn't exist
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Create the "roles" table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS roles (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT
        )
    ''')

    # Create the "user_accounts" table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_accounts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT,
            email TEXT,
            password TEXT,
            first_name TEXT,
            last_name TEXT,
            DOB DATE,
            role_id INTEGER,
            FOREIGN KEY (role_id) REFERENCES roles(ID)
        )
    ''')

    # Create the "timeslots" table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS timeslots (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            frame TEXT,
            exact_date DATE
        )
    ''')

    # Create the "bids" table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bids (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            timeslot_id INTEGER,
            user_account_id INTEGER,
            reviewed BOOLEAN,
            approved BOOLEAN,
            FOREIGN KEY (timeslot_id) REFERENCES timeslots(ID),
            FOREIGN KEY (user_account_id) REFERENCES user_accounts(ID)
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
else:
    print("Database already exists. No action taken.")
