import sys
import os
import hashlib
import json

# Find the project root directory
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Add project root to Python path
sys.path.append(PROJECT_ROOT)

# Import project modules
from agent.collector import collect_snapshot
from database.database import initialize_database, save_snapshot
from database.queries import get_latest_snapshots
from dna.change_detector import detect_changes
from dna.change_classifier import classify_change


print("===== INFRAFORENSICS PIPELINE =====")


# --------------------------------------------------
# STEP 1: Initialize Database
# --------------------------------------------------

print("\n[1] Initializing database...")

initialize_database()

print("Database ready.")


# --------------------------------------------------
# STEP 2: Collect Current System Snapshot
# --------------------------------------------------

print("\n[2] Collecting system snapshot...")

snapshot = collect_snapshot()

print("Snapshot collected.")

print("\nCurrent snapshot:")

for key, value in snapshot.items():
    print(f"{key}: {value}")


# --------------------------------------------------
# STEP 3: Generate Infrastructure DNA
# --------------------------------------------------

print("\n[3] Generating Infrastructure DNA...")


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


print("Infrastructure DNA:")
print(dna)


# --------------------------------------------------
# STEP 4: Save Snapshot
# --------------------------------------------------

print("\n[4] Saving snapshot...")

save_snapshot(snapshot)

print("Snapshot saved.")


# --------------------------------------------------
# STEP 5: Load Historical Snapshots
# --------------------------------------------------

print("\n[5] Loading historical snapshots...")

snapshots = get_latest_snapshots()

print(f"Snapshots available: {len(snapshots)}")


# --------------------------------------------------
# STEP 6: Detect Changes
# --------------------------------------------------

print("\n[6] Detecting changes...")


if len(snapshots) >= 2:

    before = snapshots[-2]

    after = snapshots[-1]

    changes = detect_changes(
        before,
        after
    )


    # --------------------------------------------------
    # STEP 7: Classify Changes
    # --------------------------------------------------

    if changes:

        print("\n===== CHANGES DETECTED =====")

        for field, old_value, new_value in changes:

            severity = classify_change(
                field,
                old_value,
                new_value
            )

            print(
                f"{field}: "
                f"{old_value} -> {new_value} "
                f"[{severity}]"
            )

    else:

        print("No changes detected.")


else:

    print("Not enough snapshots for change detection.")


# --------------------------------------------------
# PIPELINE COMPLETE
# --------------------------------------------------

print("\n===== PIPELINE COMPLETED =====")