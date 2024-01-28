# system_monitor.py
"""
Module needed for checking usages
"""

import socket
import psutil
import requests

class SystemMonitor:
    """
    needed for system monitoring.
    """

    @staticmethod
    def check_disk_usage():
        """
        Check disk usage to be more than 20%. Return as True if disk usage is above 20%, Otherwise set to False
        """
        disk_usage_percent = psutil.disk_usage('/').percent
        return disk_usage_percent > 20

    @staticmethod
    def check_cpu_utilization():
        """
        Check CPU utilization rate to be less than 75%. Return as True if CPU utilization is below 75%, Otherwise set to False
        """
        cpu_utilization = psutil.cpu_percent()
        return cpu_utilization < 75

    @staticmethod
    def check_localhost_availability():
        """
        Check availability of localhost. Return as True if localhost is available, Otherwise set to False
        """
        try:
            localhost_status = socket.gethostbyname('localhost')
            return localhost_status == '127.0.0.1'
        except socket.error:
            return False

    @staticmethod
    def check_internet_availability():
        """
        Check availability of internet by sending an HTTP request to www.google.com. Return as True if internet is available, Otherwise set to False
        """
        try:
            response = requests.get('http://www.google.com', timeout=5)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

    @staticmethod
    def jenkins_pipeline_checks():
        """
        Perform checks for a Jenkins pipeline. Determining the results.
        """
        disk_check = SystemMonitor.check_disk_usage()
        cpu_check = SystemMonitor.check_cpu_utilization()
        localhost_check = SystemMonitor.check_localhost_availability()
        internet_check = SystemMonitor.check_internet_availability()

        if disk_check and cpu_check:
            return "All is OK!"

        if not localhost_check or not internet_check:
            return "Network checks failed."

        return "ERROR! Disk or CPU usage is not within acceptable limits."

if __name__ == '__main__':
    print(SystemMonitor.jenkins_pipeline_checks())
