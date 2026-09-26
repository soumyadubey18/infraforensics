import sys
import os
import hashlib
import json

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(PROJECT_ROOT)


from agent.collector import collect_snapshot

from database.database import (
    initialize_database,
    save_snapshot
)

from database.queries import (
    get_latest_snapshots
)

from dna.change_detector import (
    detect_changes,
    compare_infrastructure_dna
)

from dna.change_classifier import (
    classify_change
)


print("===== INFRAFORENSICS PIPELINE =====")


# --------------------------------------------------
# 1. INITIALIZE DATABASE
# --------------------------------------------------

print("\n[1] Initializing database...")

initialize_database()

print("Database ready.")


# --------------------------------------------------
# 2. COLLECT SYSTEM SNAPSHOT
# --------------------------------------------------

print("\n[2] Collecting system snapshot...")

snapshot = collect_snapshot()

print("Snapshot collected.")


print("\nCurrent snapshot:")

for key, value in snapshot.items():
    print(f"{key}: {value}")


# --------------------------------------------------
# 3. GENERATE INFRASTRUCTURE DNA
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
# 4. SAVE SNAPSHOT + DNA
# --------------------------------------------------

print("\n[4] Saving snapshot and DNA...")

save_snapshot(
    snapshot,
    dna
)

print("Snapshot and DNA saved.")


# --------------------------------------------------
# 5. LOAD HISTORICAL SNAPSHOTS
# --------------------------------------------------

print("\n[5] Loading historical snapshots...")

snapshots = get_latest_snapshots()

print(
    f"Snapshots available: {len(snapshots)}"
)


# --------------------------------------------------
# 6. COMPARE INFRASTRUCTURE DNA
# --------------------------------------------------

print("\n[6] Comparing infrastructure state...")


if len(snapshots) >= 2:

    before = snapshots[-2]

    after = snapshots[-1]


    state = compare_infrastructure_dna(
        before,
        after
    )


    print("\n===== INFRASTRUCTURE STATE =====")

    print(
        f"Previous DNA : "
        f"{before['infrastructure_dna']}"
    )

    print(
        f"Current DNA  : "
        f"{after['infrastructure_dna']}"
    )

    print(
        f"State        : "
        f"{state}"
    )


    # --------------------------------------------------
    # 7. DETECT METRIC CHANGES
    # --------------------------------------------------

    print("\n[7] Detecting metric changes...")


    changes = detect_changes(
        before,
        after
    )


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

        print("No metric changes detected.")


else:

    print(
        "Not enough snapshots "
        "for infrastructure comparison."
    )


# --------------------------------------------------
# PIPELINE COMPLETE
# --------------------------------------------------

print("\n===== PIPELINE COMPLETED =====")