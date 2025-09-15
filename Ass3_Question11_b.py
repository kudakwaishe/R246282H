import sqlite3
import os

DB_FILE = 'example.db'

def setup_and_query_db():

    try:
        # Step 1: Connect to the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        print("Connected to SQLite database.")

        # Step 2: Create a table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')
        print("Table 'users' created or already exists.")

        # Step 3: Insert some data
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
        conn.commit()
        print("Data inserted and committed.")

        # Step 4: Query the data
        print("\nQuerying all users:")
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        # Step 5: Close the connection
        if conn:
            conn.close()
            print("\nConnection to database closed.")

# Run bit
# (This will create or modify the example.db file in the same directory)
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)  # Clean up from previous runs
setup_and_query_db()