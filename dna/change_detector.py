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


def compare_infrastructure_dna(before, after):

    previous_dna = before["infrastructure_dna"]

    current_dna = after["infrastructure_dna"]


    if previous_dna == current_dna:

        return "UNCHANGED"


    return "CHANGED"


if __name__ == "__main__":

    print(
        "===== INFRAFORENSICS "
        "CHANGE DETECTOR ====="
    )


    before = {

        "cpu_percent": 20,

        "memory_percent": 60,

        "disk_percent": 50,

        "process_count": 200,

        "infrastructure_dna": "DNA_ABC"
    }


    after = {

        "cpu_percent": 70,

        "memory_percent": 75,

        "disk_percent": 65,

        "process_count": 270,

        "infrastructure_dna": "DNA_XYZ"
    }


    changes = detect_changes(
        before,
        after
    )


    for field, old_value, new_value in changes:

        print(
            f"{field}: "
            f"{old_value} -> {new_value}"
        )


    state = compare_infrastructure_dna(
        before,
        after
    )


    print()

    print(
        f"Infrastructure State: "
        f"{state}"
    )