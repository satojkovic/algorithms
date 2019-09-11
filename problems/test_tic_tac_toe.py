import unittest
from tic_tac_toe import *
from nose.tools import eq_

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.toe = TicTacToe(3)
        self.toe1 = TicTacToe(2)

    def test_tic_tac_toe(self):
        eq_(self.toe.move(0, 0, 1), 0)
        eq_(self.toe.move(0, 2, 2), 0)
        eq_(self.toe.move(2, 2, 1), 0)
        eq_(self.toe.move(1, 1, 2), 0)
        eq_(self.toe.move(2, 0, 1), 0)
        eq_(self.toe.move(1, 0, 2), 0)
        eq_(self.toe.move(2, 1, 1), 1)

    def test_tic_tac_toe1(self):
        eq_(self.toe1.move(0, 0, 2), 0)
        eq_(self.toe1.move(0, 1, 1), 0)
        eq_(self.toe1.move(1, 1, 2), 2)

if __name__ == "__main__":
    unittest.main()