import unittest
from map_sum_pairs import *
from nose.tools import eq_

class TestMapSumPairs(unittest.TestCase):
    def test_map_sum_pairs1(self):
        ms1 = MapSum1()
        ms1.insert('apple', 3)
        eq_(ms1.sum('ap'), 3)
        ms1.insert('app', 2)
        eq_(ms1.sum('ap'), 5)
        ms1.insert('app', 3)
        eq_(ms1.sum('ap'), 6)

if __name__ == "__main__":
    unittest.main()