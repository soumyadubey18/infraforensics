import hashlib
import json
import sqlite3


DATABASE_NAME = "infraforensics.db"


def get_latest_snapshot():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            hostname,
            cpu_percent,
            memory_percent,
            disk_percent,
            process_count
        FROM system_snapshots
        ORDER BY id DESC
        LIMIT 1
    """)

    snapshot = cursor.fetchone()

    connection.close()

    if snapshot is None:
        return None

    return dict(snapshot)


def generate_dna(snapshot):
    """
    Generate a unique fingerprint for an infrastructure snapshot.
    """

    snapshot_data = {
        "hostname": snapshot["hostname"],
        "cpu_percent": snapshot["cpu_percent"],
        "memory_percent": snapshot["memory_percent"],
        "disk_percent": snapshot["disk_percent"],
        "process_count": snapshot["process_count"]
    }

    normalized_data = json.dumps(
        snapshot_data,
        sort_keys=True
    )

    dna = hashlib.sha256(
        normalized_data.encode("utf-8")
    ).hexdigest()

    return dna


if __name__ == "__main__":

    snapshot = get_latest_snapshot()

    if snapshot is None:
        print("No infrastructure snapshot found.")
    else:
        dna = generate_dna(snapshot)

        print("===== INFRAFORENSICS =====")
        print("Latest Infrastructure Snapshot")
        print("--------------------------------")
        print(f"Hostname      : {snapshot['hostname']}")
        print(f"CPU           : {snapshot['cpu_percent']}%")
        print(f"Memory        : {snapshot['memory_percent']}%")
        print(f"Disk          : {snapshot['disk_percent']}%")
        print(f"Processes     : {snapshot['process_count']}")
        print()
        print(f"Infrastructure DNA:")
        print(dna)