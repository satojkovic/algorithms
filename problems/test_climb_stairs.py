import unittest
from climb_stairs import *
from nose.tools import eq_

class TestClimbStairs(unittest.TestCase):
    def test_climb_stairs1(self):
        eq_(climb_stairs1(3), 3)
        eq_(climb_stairs1(0), 1)
        eq_(climb_stairs1(5), 8)
        eq_(climb_stairs1(-1), 0)
        eq_(climb_stairs1(1), 1)

    def test_climb_stairs2(self):
        eq_(climb_stairs2(3), 3)
        eq_(climb_stairs2(0), 1)
        eq_(climb_stairs2(5), 8)
        eq_(climb_stairs2(-1), 0)
        eq_(climb_stairs2(1), 1)
        eq_(climb_stairs2(30), 1346269)

    def test_climb_stairs3(self):
        eq_(climb_stairs3(3), 3)
        eq_(climb_stairs3(0), 1)
        eq_(climb_stairs3(5), 8)
        eq_(climb_stairs3(-1), 0)
        eq_(climb_stairs3(1), 1)
        eq_(climb_stairs3(30), 1346269)

if __name__ == "__main__":
    unittest.main()
