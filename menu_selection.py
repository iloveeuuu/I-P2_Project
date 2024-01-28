import unittest
from unittest.mock import patch, MagicMock
import requests
from menu_selection import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    
    @patch('psutil.disk_usage')
    def test_disk_usage_below_threshold(self, mock_disk_usage):
        # Given
        mock_disk_usage.return_value.percent = 25
        monitor = SystemMonitor()

        # When
        result = monitor.check_disk_usage()

        # Then
        self.assertTrue(result)

    @patch('psutil.cpu_percent')
    def test_high_cpu_utilization(self, mock_cpu_percent):
        # Given
        mock_cpu_percent.return_value = 80
        monitor = SystemMonitor()

        # When
        result = monitor.check_cpu_utilization()

        # Then
        self.assertFalse(result)

    @patch('psutil.net_if_addrs')
    def test_localhost_available(self, mock_net_if_addrs):
        # Given
        mock_net_if_addrs.return_value = {'lo': MagicMock()}

        # When
        result = SystemMonitor.check_localhost_availability()

        # Then
        self.assertTrue(result)

    @patch('requests.get')
    def test_internet_available_with_connection(self, mock_requests_get):
        # Given
        mock_response = MagicMock(status_code=200)
        mock_requests_get.return_value = mock_response

        # When
        result = SystemMonitor.check_internet_availability()

        # Then
        self.assertTrue(result)

    @patch('requests.get', side_effect=requests.ConnectionError)
    def test_internet_unavailable_without_connection(self, mock_requests_get):
        # When
        result = SystemMonitor.check_internet_availability()

        # Then
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
