import subprocess
import sys


if __name__ == "__main__":

    print("========================================")
    print("        INFRAFORENSICS")
    print("========================================")

    print("\nStarting infrastructure forensic pipeline...\n")

    result = subprocess.run(
        [
            sys.executable,
            "pipeline/run_pipeline.py"
        ]
    )

    print("\n========================================")

    if result.returncode == 0:
        print("INFRAFORENSICS PIPELINE COMPLETED")
    else:
        print("INFRAFORENSICS PIPELINE FAILED")

    print("========================================")