import unittest
from move_zeros import move_zeros1, move_zeros2, move_zeros3, move_zeros4
from nose.tools import eq_

class TestMoveZeros(unittest.TestCase):
    def test_move_zeros1(self):
        nums = [0, 1, 0, 3, 12]
        eq_(move_zeros1(nums), [1, 3, 12, 0, 0])

    def test_move_zeros2(self):
        nums = [0, 1, 0, 3, 12]
        eq_(move_zeros2(nums), [1, 3, 12, 0, 0])

    def test_move_zeros3(self):
        nums = [0, 1, 0, 3, 12]
        eq_(move_zeros3(nums), [1, 3, 12, 0, 0])

    def test_move_zeros4(self):
        nums = [0, 1, 0, 3, 12]
        eq_(move_zeros4(nums), [1, 3, 12, 0, 0])

if __name__ == "__main__":
    unittest.main()