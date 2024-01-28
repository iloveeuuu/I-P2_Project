# test_system_monitor.py
"""
Unit tests for the SystemMonitor class in system_monitor.py.
"""

import unittest
from unittest.mock import patch, MagicMock
import requests
from system_monitor import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    """
    Test cases for the SystemMonitor class.
    """

    @patch('psutil.disk_usage')
    def test_check_disk_usage(self, mock_disk_usage):
        """
        Test check_disk_usage method.

        Mocks the disk usage to be 25% and asserts that the method returns True.
        """
        mock_disk_usage.return_value.percent = 25
        monitor = SystemMonitor()
        result = monitor.check_disk_usage()
        self.assertTrue(result)

    @patch('psutil.cpu_percent')
    def test_check_cpu_utilization(self, mock_cpu_percent):
        """
        Test check_cpu_utilization method.

        Mocks the CPU utilization to be 70% and asserts that the method returns True.
        """
        mock_cpu_percent.return_value = 70
        monitor = SystemMonitor()
        result = monitor.check_cpu_utilization()
        self.assertTrue(result)

    @patch('psutil.net_if_addrs')
    def test_check_localhost_availability(self, mock_net_if_addrs):
        """
        Test check_localhost_availability method.

        Mocks the presence of 'lo' interface and asserts that the method returns True.
        """
        mock_net_if_addrs.return_value = {'lo': MagicMock()}
        result = SystemMonitor.check_localhost_availability()
        self.assertTrue(result)

    @patch('requests.get')
    def test_check_internet_availability_with_connection(self, mock_requests_get):
        """
        Test check_internet_availability method with a successful HTTP request.

        Mocks a successful HTTP request to www.google.com and asserts that the method returns True.
        """
        mock_response = MagicMock(status_code=200)
        mock_requests_get.return_value = mock_response
        result = SystemMonitor.check_internet_availability()
        self.assertTrue(result)

    @patch('requests.get', side_effect=requests.ConnectionError)
    def test_check_internet_availability_without_connection(self, mock_requests_get):
        """
        Test check_internet_availability method without a successful HTTP request.

        Mocks a ConnectionError during an HTTP request and asserts that the method returns False.
        """
        result = SystemMonitor.check_internet_availability()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
