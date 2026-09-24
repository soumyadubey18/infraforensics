import sqlite3


DATABASE_NAME = "infraforensics.db"


def get_last_two_snapshots():
    connection = sqlite3.connect(DATABASE_NAME)
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
        FROM system_snapshots
        ORDER BY id DESC
        LIMIT 2
    """)

    snapshots = cursor.fetchall()

    connection.close()

    return snapshots


def compare_snapshots(previous, current):
    changes = {}

    fields = [
        "cpu_percent",
        "memory_percent",
        "disk_percent",
        "process_count"
    ]

    for field in fields:
        old_value = previous[field]
        new_value = current[field]

        if old_value != new_value:
            changes[field] = {
                "before": old_value,
                "after": new_value
            }

    return changes


if __name__ == "__main__":

    snapshots = get_last_two_snapshots()

    if len(snapshots) < 2:
        print("At least two snapshots are required.")
    else:
        previous = snapshots[1]
        current = snapshots[0]

        changes = compare_snapshots(previous, current)

        print("===== INFRAFORENSICS CHANGE DETECTION =====")
        print()

        if not changes:
            print("No infrastructure changes detected.")
        else:
            print("Infrastructure changes detected:")
            print()

            for field, change in changes.items():
                print(
                    f"{field}: "
                    f"{change['before']} → {change['after']}"
                )