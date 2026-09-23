import psutil
import socket
from datetime import datetime


def collect_system_health():
    health = {
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
        "process_count": len(psutil.pids())
    }

    return health


if __name__ == "__main__":
    data = collect_system_health()

    print("===== INFRAFORENSICS SYSTEM HEALTH =====")
    print(f"Timestamp      : {data['timestamp']}")
    print(f"Hostname       : {data['hostname']}")
    print(f"CPU Usage      : {data['cpu_percent']}%")
    print(f"Memory Usage   : {data['memory_percent']}%")
    print(f"Disk Usage     : {data['disk_percent']}%")
    print(f"Process Count  : {data['process_count']}")