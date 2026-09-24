import psutil
import socket
from datetime import datetime


def collect_snapshot():
    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "process_count": len(psutil.pids())
    }

    return snapshot


if __name__ == "__main__":

    print("===== INFRAFORENSICS SYSTEM SNAPSHOT =====")

    snapshot = collect_snapshot()

    for key, value in snapshot.items():
        print(f"{key}: {value}")