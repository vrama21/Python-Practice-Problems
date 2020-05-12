import unittest
from Easy.Array.array import *

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

    def test_getReversed(self):
        self.assertEqual(getReversed(array), [False, '3', 5, True, 'Test', 1])

    def test_countElementInArray(self):
        _list = ['A', 'A', 'C', 'D', 'E',
                 'E', 'A', 'B', 'B', 'A']
        self.assertEqual(countElementInArray(_list, 'A'), 4)


if __name__ == '__main__':
    unittest.main()
