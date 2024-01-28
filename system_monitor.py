# system_monitor.py
"""
Module for monitoring system status.
"""

import socket
import psutil
import requests

class SystemMonitor:
    """
    Class providing methods for system monitoring.
    """

    @staticmethod
    def check_disk_usage():
        """
        Check disk usage to be more than 20%.

        Returns:
            bool: True if disk usage is above 20%, False otherwise.
        """
        disk_usage_percent = psutil.disk_usage('/').percent
        return disk_usage_percent > 20

    @staticmethod
    def check_cpu_utilization():
        """
        Check CPU utilization rate to be less than 75%.

        Returns:
            bool: True if CPU utilization is below 75%, False otherwise.
        """
        cpu_utilization = psutil.cpu_percent()
        return cpu_utilization < 75

    @staticmethod
    def check_localhost_availability():
        """
        Check availability of localhost.

        Returns:
            bool: True if localhost is available, False otherwise.
        """
        try:
            localhost_info = psutil.net_if_addrs()['lo']
            return any(addr.family == socket.AF_INET for addr in localhost_info)
        except KeyError:
            return False

    @staticmethod
    def check_internet_availability():
        """
        Check availability of internet by sending an HTTP request to www.google.com.

        Returns:
            bool: True if internet is available, False otherwise.
        """
        try:
            response = requests.get('http://www.google.com', timeout=5)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

    @staticmethod
    def jenkins_pipeline_checks():
        """
        Perform checks for a Jenkins pipeline.

        Returns:
            str: Result message indicating the status of checks.
        """
        disk_check = SystemMonitor.check_disk_usage()
        cpu_check = SystemMonitor.check_cpu_utilization()
        localhost_check = SystemMonitor.check_localhost_availability()
        internet_check = SystemMonitor.check_internet_availability()

        if disk_check and cpu_check:
            return "Everything is OK!"

        if not localhost_check or not internet_check:
            return "Network checks failed."

        return "ERROR! Disk or CPU usage is not within acceptable limits."

if __name__ == '__main__':
    print(SystemMonitor.jenkins_pipeline_checks())
