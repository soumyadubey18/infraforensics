import sqlite3
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DB_PATH = os.path.join(
    BASE_DIR,
    "database",
    "infraforensics.db"
)


def get_connection():
    return sqlite3.connect(DB_PATH)


def get_latest_snapshots(limit=2):

    connection = get_connection()

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
            process_count,
            infrastructure_dna
        FROM snapshots
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    connection.close()

    return list(reversed(rows))


def get_all_snapshots():

    connection = get_connection()

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
            process_count,
            infrastructure_dna
        FROM snapshots
        ORDER BY id ASC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows


if __name__ == "__main__":

    snapshots = get_all_snapshots()

    print()
    print("========================================")
    print("       INFRAFORENSICS HISTORY")
    print("========================================")

    print(
        f"\nTotal snapshots stored: "
        f"{len(snapshots)}"
    )

    for snapshot in snapshots:

        print()
        print("----------------------------------------")

        print(
            f"Snapshot ID : "
            f"{snapshot['id']}"
        )

        print(
            f"Timestamp   : "
            f"{snapshot['timestamp']}"
        )

        print(
            f"Hostname    : "
            f"{snapshot['hostname']}"
        )

        print(
            f"CPU         : "
            f"{snapshot['cpu_percent']}%"
        )

        print(
            f"Memory      : "
            f"{snapshot['memory_percent']}%"
        )

        print(
            f"Disk        : "
            f"{snapshot['disk_percent']}%"
        )

        print(
            f"Processes   : "
            f"{snapshot['process_count']}"
        )

        print(
            f"DNA         : "
            f"{snapshot['infrastructure_dna']}"
        )

    print()
    print("========================================")
    print("        END OF FORENSIC HISTORY")
    print("========================================")