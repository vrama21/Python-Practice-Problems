import unittest
from Easy.Problem1.math import *

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()

