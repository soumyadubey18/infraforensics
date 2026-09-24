import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "infraforensics.db")


def get_latest_snapshots(limit=2):

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            timestamp,
            hostname,
            cpu_percent,
            memory_percent,
            disk_percent,
            process_count
        FROM snapshots
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    connection.close()

    # Return oldest → newest
    return list(reversed(rows))


if __name__ == "__main__":

    snapshots = get_latest_snapshots()

    print("===== LATEST SNAPSHOTS =====")

    for snapshot in snapshots:
        print(dict(snapshot))