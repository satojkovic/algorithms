import unittest
from top_k_freq import *
from nose.tools import eq_

class TestTopKFreq(unittest.TestCase):
    def test_top_k_freq1(self):
        eq_(top_k_freq1([1, 1, 1, 2, 2, 3], 2), [1, 2])
        eq_(top_k_freq1([1], 1), [1])
        eq_(top_k_freq1([], 3), [])
        eq_(top_k_freq1([1, 2], 2), [1, 2])

if __name__ == "__main__":
    unittest.main()