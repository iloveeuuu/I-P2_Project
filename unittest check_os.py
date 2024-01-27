import unittest
from unittest.mock import patch
from your_system_monitor_script import SystemMonitor

class TestSystemMonitor(unittest.TestCase):

    def test_disk_usage(self):
        monitor = SystemMonitor()

        # Mocking psutil.disk_usage to return specific values
        with patch('psutil.disk_usage') as mock_disk_usage:
            mock_disk_usage.return_value.percent = 30
            self.assertTrue(monitor.check_disk_usage(20))

            mock_disk_usage.return_value.percent = 90
            self.assertFalse(monitor.check_disk_usage(20))

    def test_cpu_utilization(self):
        monitor = SystemMonitor()

        # Mocking psutil.cpu_percent to return specific values
        with patch('psutil.cpu_percent') as mock_cpu_percent:
            mock_cpu_percent.return_value = 50
            self.assertTrue(monitor.check_cpu_utilization(75))

            mock_cpu_percent.return_value = 10
            self.assertFalse(monitor.check_cpu_utilization(75))

    def test_localhost(self):
        monitor = SystemMonitor()

        # Mocking socket.create_connection to succeed
        with patch('socket.create_connection'):
            self.assertTrue(monitor.check_localhost())

        # Mocking socket.create_connection to raise an exception
        with patch('socket.create_connection', side_effect=socket.error):
            self.assertFalse(monitor.check_localhost())

    def test_internet_access(self):
        monitor = SystemMonitor()

        # Mocking requests.get to succeed
        with patch('requests.get'):
            self.assertTrue(monitor.check_internet_access())

        # Mocking requests.get to raise an exception
        with patch('requests.get', side_effect=requests.ConnectionError):
            self.assertFalse(monitor.check_internet_access())

if __name__ == '__main__':
    unittest.main()
