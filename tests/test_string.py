import unittest
from Easy.String.string import *


class Test(unittest.TestCase):
    def test_convertToInt(self):
        self.assertEquals(convertToInt('5'), 5)

    def test_isStringEmpty(self):    
        self.assertEquals(isStringEmpty(''), True)
        self.assertEquals(isStringEmpty('Not Empty'), False)

    def test_concatenate(self):
        self.assertEquals(concatenate('concat', 'enate'), 'concatenate')

    def test_strLength(self):
        self.assertEquals(strLength('teststring'), 10)

    def test_separateString(self):
        string = 'Lets separate this string into an array'
        answer = ['Lets', 'separate', 'this', 'string', 'into', 'an', 'array']
        self.assertEquals(separateString(string), answer)

    def test_joinString(self):
        string = ['Lets', 'join', 'this', 'array', 'into', 'a', 'string']
        answer = 'Lets join this array into a string'
        self.assertEquals(joinString(string), answer)

if __name__ == '__main__':
    unittest.main()
