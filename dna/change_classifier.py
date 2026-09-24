def classify_change(field, before, after):
    if field == "cpu_percent":
        difference = abs(after - before)

        if difference >= 50:
            return "MEDIUM"

        return "LOW"

    if field == "memory_percent":
        difference = abs(after - before)

        if difference >= 20:
            return "HIGH"

        if difference >= 10:
            return "MEDIUM"

        return "LOW"

    if field == "disk_percent":
        difference = after - before

        if difference >= 20:
            return "HIGH"

        if difference >= 10:
            return "MEDIUM"

        return "LOW"

    if field == "process_count":
        difference = abs(after - before)

        if difference >= 50:
            return "MEDIUM"

        return "LOW"

    return "LOW"


if __name__ == "__main__":
    print("===== INFRAFORENSICS CHANGE CLASSIFIER =====")

    examples = [
        ("cpu_percent", 20, 25),
        ("memory_percent", 60, 75),
        ("disk_percent", 50, 75),
        ("process_count", 200, 270)
    ]

    for field, before, after in examples:
        severity = classify_change(field, before, after)

        print(
            f"{field}: "
        f"{before} -> {after} "
            f"[{severity}]"
        )