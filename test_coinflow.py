# test_coinflow.py
"""
Tests for CoinFlow module.
"""

import unittest
from coinflow import CoinFlow

class TestCoinFlow(unittest.TestCase):
    """Test cases for CoinFlow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinFlow()
        self.assertIsInstance(instance, CoinFlow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinFlow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
