import unittest
from rearrange_str import *
from nose.tools import eq_

class TestRearrangeStr(unittest.TestCase):
    def test_rearrange_str(self):
        eq_(rearrange_str('dcc'), 'cdc')
        eq_(rearrange_str('aaba'), '')
        eq_(rearrange_str('caccd'), 'cacdc')

if __name__ == "__main__":
    unittest.main()