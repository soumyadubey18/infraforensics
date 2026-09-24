def detect_changes(before, after):
    changes = []

    fields = [
        "cpu_percent",
        "memory_percent",
        "disk_percent",
        "process_count"
    ]

    for field in fields:

        old_value = before[field]
        new_value = after[field]

        if old_value != new_value:
            changes.append(
                (
                    field,
                    old_value,
                    new_value
                )
            )

    return changes


if __name__ == "__main__":

    print("===== INFRAFORENSICS CHANGE DETECTOR =====")

    before = {
        "cpu_percent": 20,
        "memory_percent": 60,
        "disk_percent": 50,
        "process_count": 200
    }

    after = {
        "cpu_percent": 70,
        "memory_percent": 75,
        "disk_percent": 65,
        "process_count": 270
    }

    changes = detect_changes(before, after)

    for field, old_value, new_value in changes:
        print(
            f"{field}: "
            f"{old_value} -> {new_value}"
        )