import unittest
from hamming_weight import *
from nose.tools import eq_

class TestHammingWeight(unittest.TestCase):
    def test_hamming_weight(self):
        eq_(hamming_weight(11), 3)
        eq_(hamming_weight(0), 0)
        eq_(hamming_weight(4294967295), 32)
        eq_(hamming_weight(4294967296), 1)

if __name__ == "__main__":
    unittest.main()