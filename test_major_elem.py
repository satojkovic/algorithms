import unittest
from major_elem import major_elem1
from nose.tools import eq_

class TestMajorElem(unittest.TestCase):
    def setUp(self):
        self.nums1 = [2, 1, 2]
        self.nums2 = [3, 3, 3, 1, 1, 3, 1]
        self.nums3 = [0, 0, 0]

    def test_major_elem1(self):
        eq_(major_elem1(self.nums1), 2)
        eq_(major_elem1(self.nums2), 3)
        eq_(major_elem1(self.nums3), 0)

if __name__ == "__main__":
    unittest.main()
