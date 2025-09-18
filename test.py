# print("hello dosto kaise ho sab")
# print("good luck zBihiregdfvkjhib")
# print("good luck zBihiregdfvkjhib")

"""
test.py
This module contains unit tests for demo.py.
"""

import unittest
from demo import greet

class TestDemo(unittest.TestCase):
    """Unit test class for demo.py."""

    def test_greet(self):
        """Test if greet function returns correct message."""
        self.assertEqual(greet("Aryan"), "Hello, Aryan!")

if __name__ == "__main__":
    unittest.main()

 
