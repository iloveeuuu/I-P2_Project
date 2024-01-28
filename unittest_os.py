import unittest
from unittest.mock import patch, MagicMock
import requests
from menu_selection import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    @patch('psutil.disk_usage')
    def test_check_disk_usage(self, mock_disk_usage):
        mock_disk_usage.return_value.percent = 25
        monitor = SystemMonitor()
        self.assertTrue(monitor.check_disk_usage())

    @patch('psutil.cpu_percent')
    def test_check_cpu_utilization(self, mock_cpu_percent):
        mock_cpu_percent.return_value = 80
        monitor = SystemMonitor()
        self.assertFalse(monitor.check_cpu_utilization())

    @patch('psutil.net_if_addrs')
    def test_check_localhost_availability(self, mock_net_if_addrs):
        mock_net_if_addrs.return_value = {'lo': MagicMock()}
        result = SystemMonitor.check_localhost_availability()
        self.assertTrue(result)

    @patch('requests.get')
    def test_check_internet_availability_with_connection(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response
        result = SystemMonitor.check_internet_availability()
        self.assertTrue(result)

    @patch('requests.get', side_effect=requests.ConnectionError)
    def test_check_internet_availability_without_connection(self, mock_requests_get):
        result = SystemMonitor.check_internet_availability()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
