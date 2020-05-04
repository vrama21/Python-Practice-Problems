import unittest
from Easy.Problem2.problem2 import *

array = [1, 'Test', True, 5, '3', False]

class Test(unittest.TestCase):
    def test_getFirstElement(self):
        self.assertEqual(getFirstElement(array), 1)

    def test_getLastElement(self):
        self.assertEqual(getLastElement(array), False)

    def test_getFirstThreeElements(self):
        self.assertEqual(getFirstThreeElements(array), [1, 'Test', True])
        
    def test_getLastThreeElements(self):
        self.assertEqual(getLastThreeElements(array), [5, '3', False])
    
    def test_getIntegers(self):
        self.assertEqual(getIntegers(array), [1, 5])

    def test_getStrings(self):
        self.assertEqual(getStrings(array), ['Test', '3'])

    def test_getBooleans(self):
        self.assertEqual(getBooleans(array), [True, False])

if __name__ == '__main__':
    unittest.main()

