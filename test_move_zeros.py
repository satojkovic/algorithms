import unittest
from move_zeros import move_zeros1, move_zeros2, move_zeros3, move_zeros4
from nose.tools import eq_

class TestMoveZeros(unittest.TestCase):
    def setUp(self):
        self.test_cases = []
        self.test_cases.append([0, 1, 0, 3, 12])
        self.test_cases.append([0])
        self.test_cases.append([1])

        self.results = []
        self.results.append([1, 3, 12, 0, 0])
        self.results.append([0])
        self.results.append([1])

    def test_move_zeros1(self):
        for test_case, result in zip(self.test_cases, self.results):
            eq_(move_zeros1(test_case), result)

    def test_move_zeros2(self):
        for test_case, result in zip(self.test_cases, self.results):
            eq_(move_zeros2(test_case), result)

    def test_move_zeros3(self):
        for test_case, result in zip(self.test_cases, self.results):
            eq_(move_zeros3(test_case), result)

    def test_move_zeros4(self):
        for test_case, result in zip(self.test_cases, self.results):
            eq_(move_zeros4(test_case), result)

if __name__ == "__main__":
    unittest.main()