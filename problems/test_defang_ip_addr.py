import unittest
from defang_ip_addr import *
from nose.tools import eq_

class TestDefangIpAddr(unittest.TestCase):
    def test_defang_ip_addr1(self):
        eq_(defang_ip_addr1('1.1.1.1'), '1[.]1[.]1[.]1')
        eq_(defang_ip_addr1('255.100.25.0'), '255[.]100[.]25[.]0')
        eq_(defang_ip_addr1('0.0.0.0'), '0[.]0[.]0[.]0')

if __name__ == "__main__":
    unittest.main()