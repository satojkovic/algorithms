import unittest
from shuffle_an_array import *
from nose.tools import eq_

class TestShuffleAnArray(unittest.TestCase):
    def setUp(self):
        # Normal case
        self.obj = ShuffleAnArray([1, 2, 3])
        self.obj2 = ShuffleAnArray([52, 104, -19, 0])
        # Extreme case
        self.obj3 = ShuffleAnArray([])
        # illegal input
        # strange input

    def test_shuffle_an_array1(self):
        self.assertCountEqual(self.obj.shuffle(), [1, 2, 3])
        eq_(self.obj.reset(), [1, 2, 3])

    def test_shuffle_an_array2(self):
        self.assertCountEqual(self.obj2.shuffle(), [52, 104, -19, 0])
        eq_(self.obj2.reset(), [52, 104, -19, 0])

    def test_shuffle_an_array3(self):
        eq_(self.obj3.shuffle(), [])
        eq_(self.obj3.reset(), [])

if __name__ == "__main__":
    unittest.main()