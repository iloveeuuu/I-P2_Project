# jenkins_system_monitor.py
import psutil
import requests

class JenkinsSystemMonitor:
    @staticmethod
    def check_disk_usage():
        disk_usage_percent = psutil.disk_usage('/').percent
        return disk_usage_percent > 20

    @staticmethod
    def check_cpu_utilization():
        cpu_utilization = psutil.cpu_percent()
        return cpu_utilization < 75

    @staticmethod
    def check_localhost_availability():
        try:
            localhost_info = psutil.net_if_addrs()['lo']
            return any(addr.family == psutil.AF_INET for addr in localhost_info)
        except KeyError:
            return False

    @staticmethod
    def check_internet_availability():
        try:
            response = requests.get('http://www.google.com', timeout=5)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

    @staticmethod
    def jenkins_pipeline_checks():
        disk_check = JenkinsSystemMonitor.check_disk_usage()
        cpu_check = JenkinsSystemMonitor.check_cpu_utilization()
        localhost_check = JenkinsSystemMonitor.check_localhost_availability()
        internet_check = JenkinsSystemMonitor.check_internet_availability()

        if disk_check and cpu_check:
            return "Everything is OK!"
        elif not localhost_check or not internet_check:
            return "Network checks failed."
        else:
            return "ERROR! Disk or CPU usage is not within acceptable limits."

if __name__ == '__main__':
    print(JenkinsSystemMonitor.jenkins_pipeline_checks())
