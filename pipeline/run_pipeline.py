import sys
import os

# Add INFRAFORENSICS project root to Python path
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)


from agent.collector import collect_snapshot
from database.database import initialize_database, save_snapshot
from database.queries import get_latest_snapshots
from dna.change_detector import detect_changes


print("===== INFRAFORENSICS PIPELINE =====")


# --------------------------------------------------
# STEP 1: Initialize database
# --------------------------------------------------

print("\n[1] Initializing database...")

initialize_database()

print("Database ready.")


# --------------------------------------------------
# STEP 2: Collect current system snapshot
# --------------------------------------------------

print("\n[2] Collecting system snapshot...")

snapshot = collect_snapshot()

print("Snapshot collected.")


# --------------------------------------------------
# STEP 3: Save snapshot
# --------------------------------------------------

print("\n[3] Saving snapshot...")

save_snapshot(snapshot)

print("Snapshot saved.")


# --------------------------------------------------
# STEP 4: Load historical snapshots
# --------------------------------------------------

print("\n[4] Loading historical snapshots...")

snapshots = get_latest_snapshots()

print(f"Snapshots available: {len(snapshots)}")


# --------------------------------------------------
# STEP 5: Detect changes
# --------------------------------------------------

print("\n[5] Detecting changes...")

if len(snapshots) >= 2:

    before = snapshots[-2]
    after = snapshots[-1]

    changes = detect_changes(before, after)

    if changes:

        print("\n===== CHANGES DETECTED =====")

        for field, old_value, new_value in changes:

            print(
                f"{field}: "
                f"{old_value} -> {new_value}"
            )

    else:

        print("No changes detected.")

else:

    print(
        "Not enough snapshots "
        "for change detection."
    )


print("\n===== PIPELINE COMPLETED =====")