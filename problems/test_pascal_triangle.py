import unittest
from pascal_triangle import *
from nose.tools import eq_

class TestPascalTriangle(unittest.TestCase):
    def test_pascal_triangle1(self):
        eq_(pascal_triangle1(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
        eq_(pascal_triangle1(1), [[1]])
        eq_(pascal_triangle1(0), [])

if __name__ == "__main__":
    unittest.main()
