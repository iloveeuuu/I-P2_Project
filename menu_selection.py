import psutil
import socket
import requests

class SystemMonitor:
    def __init__(self):
        pass

    @staticmethod
    def check_disk_usage(threshold_percentage):
        disk_usage = psutil.disk_usage('/')
        return disk_usage.percent > threshold_percentage

    @staticmethod
    def check_cpu_utilization(threshold_percentage):
        cpu_utilization = psutil.cpu_percent()
        return cpu_utilization < threshold_percentage

    @staticmethod
    def check_localhost():
        try:
            socket.create_connection(("localhost", 80), timeout=2)
            return True
        except (socket.error, socket.timeout):
            return False

    @staticmethod
    def check_internet_access():
        try:
            requests.get("http://www.google.com", timeout=2)
            return True
        except requests.ConnectionError:
            return False

def perform_system_checks():
    monitor = SystemMonitor()

    disk_check = monitor.check_disk_usage(20)
    cpu_check = monitor.check_cpu_utilization(75)
    localhost_check = monitor.check_localhost()
    internet_check = monitor.check_internet_access()

    if disk_check or cpu_check:
        print("ERROR! Disk usage or CPU usage failed.")
    elif localhost_check and internet_check:
        print("Everything is OK.")
    else:
        print("Network checks failed.")

def test_system_monitor():
    monitor = SystemMonitor()

    # Test Disk Usage Check
    assert monitor.check_disk_usage(30) is True
    assert monitor.check_disk_usage(90) is False

    # Test CPU Utilization Check
    assert monitor.check_cpu_utilization(50) is True
    assert monitor.check_cpu_utilization(10) is False

    # Test Localhost Check
    assert monitor.check_localhost() is True

    # Test Internet Access Check
    assert monitor.check_internet_access() is True

if __name__ == "__main__":
    perform_system_checks()
    test_system_monitor()
