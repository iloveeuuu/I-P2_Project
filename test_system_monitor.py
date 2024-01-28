# test_system_monitor.py
import unittest
from unittest.mock import patch, MagicMock
from system_monitor import SystemMonitor

class TestSystemMonitor(unittest.TestCase):

    def test_check_disk_usage(self):
        with patch('psutil.disk_usage') as mock_disk_usage:
            # Given
            mock_disk_usage.return_value.percent = 25

            # When
            result = SystemMonitor.check_disk_usage()

            # Then
            self.assertTrue(result)

    def test_check_cpu_utilization(self):
        with patch('psutil.cpu_percent') as mock_cpu_percent:
            # Given
            mock_cpu_percent.return_value = 50

            # When
            result = SystemMonitor.check_cpu_utilization()

            # Then
            self.assertTrue(result)

    def test_check_localhost_availability(self):
        with patch('psutil.net_if_addrs') as mock_net_if_addrs:
            # Given
            mock_net_if_addrs.return_value = {'lo': MagicMock()}

            # When
            result = SystemMonitor.check_localhost_availability()

            # Then
            self.assertTrue(result)

    def test_check_internet_availability(self):
        with patch('requests.get') as mock_requests_get:
            # Given
            mock_response = MagicMock(status_code=200)
            mock_requests_get.return_value = mock_response

            # When
            result = SystemMonitor.check_internet_availability()

            # Then
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
