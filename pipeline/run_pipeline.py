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


print("===== INFRAFORENSICS PIPELINE =====")


# --------------------------------------------------
# STEP 1: Initialize database
# --------------------------------------------------

print("\n[1] Initializing database...")

initialize_database()

print("Database ready.")


# --------------------------------------------------
# STEP 2: Collect system snapshot
# --------------------------------------------------

print("\n[2] Collecting system snapshot...")

snapshot = collect_snapshot()

print("Snapshot collected.")


# --------------------------------------------------
# STEP 3: Save snapshot
# --------------------------------------------------

print("\n[3] Saving snapshot to database...")

save_snapshot(snapshot)

print("Snapshot saved successfully.")


# --------------------------------------------------
# Display snapshot
# --------------------------------------------------

print("\n===== CURRENT INFRASTRUCTURE STATE =====")

for key, value in snapshot.items():
    print(f"{key}: {value}")


print("\n===== PIPELINE STEP 2 COMPLETED =====")