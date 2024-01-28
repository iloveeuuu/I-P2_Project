"""Module for handling menu selection."""
import socket
import psutil
import requests

class SystemMonitor:
    """Class for monitoring system resources and network connectivity."""
    @staticmethod
    def check_disk_usage():
        """Check disk usage and return True if it's below 20%."""
        disk_usage = psutil.disk_usage('/')
        return disk_usage.percent > 20

    @staticmethod
    def check_cpu_utilization():
        """Check CPU utilization and return True if it's below 75%."""
        cpu_utilization = psutil.cpu_percent()
        return cpu_utilization < 75

    @staticmethod
    def check_localhost_availability():
        """Check if localhost is available and return True if it is."""
        try:
            localhost_status = socket.gethostbyname('localhost')
            return localhost_status == '127.0.0.1'
        except socket.error:
            return False

    @staticmethod
    def check_internet_availability():
        """Check internet availability and return True if it's available."""
        try:
            response = requests.get("http://www.google.com", timeout=5)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

def main():
    """Disk and CPU."""
    monitor = SystemMonitor()

    disk_status = monitor.check_disk_usage()
    cpu_status = monitor.check_cpu_utilization()
    localhost_status = monitor.check_localhost_availability()
    internet_status = monitor.check_internet_availability()

    if not disk_status or not cpu_status:
        print("ERROR! Disk usage or CPU utilization exceeded thresholds.")
    elif localhost_status and internet_status:
        print("Everything is OK.")
    else:
        print("Network checks failed.")

if __name__ == "__main__":
    main()
