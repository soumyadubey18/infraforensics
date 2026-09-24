import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "infraforensics.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            hostname TEXT,
            cpu_percent REAL,
            memory_percent REAL,
            disk_percent REAL,
            process_count INTEGER
        )
    """)

    connection.commit()
    connection.close()


def save_snapshot(snapshot):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO snapshots (
            timestamp,
            hostname,
            cpu_percent,
            memory_percent,
            disk_percent,
            process_count
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        snapshot["timestamp"],
        snapshot["hostname"],
        snapshot["cpu_percent"],
        snapshot["memory_percent"],
        snapshot["disk_percent"],
        snapshot["process_count"]
    ))

    connection.commit()
    connection.close()


if __name__ == "__main__":

    initialize_database()

    print("Database initialized successfully.")