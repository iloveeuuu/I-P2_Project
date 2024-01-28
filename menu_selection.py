import unittest
from unittest.mock import patch, MagicMock, Mock
import requests
from menu_selection import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = SystemMonitor()

    @patch('psutil.disk_usage', return_value=Mock(percent=25))
    def test_check_disk_usage(self, _):
        self.assertTrue(self.monitor.check_disk_usage())

    @patch('psutil.cpu_percent', return_value=80)
    def test_check_cpu_utilization(self, _):
        self.assertFalse(self.monitor.check_cpu_utilization())

    @patch('psutil.net_if_addrs', return_value={'lo': MagicMock()})
    def test_check_localhost_availability(self, _):
        self.assertTrue(SystemMonitor.check_localhost_availability())

    @patch('requests.get', return_value=MagicMock(status_code=200))
    def test_check_internet_availability_with_connection(self, _):
        self.assertTrue(SystemMonitor.check_internet_availability())

    @patch('requests.get', side_effect=requests.ConnectionError)
    def test_check_internet_availability_without_connection(self, _):
        self.assertFalse(SystemMonitor.check_internet_availability())

if __name__ == '__main__':
    unittest.main()
