from src.gcd_string import *

def test_gcd_string():
    assert gcd_string("ABABAB", "ABAB") == "AB"
    assert gcd_string("LEET", "CODE") == ""
    assert gcd_string("ABCABC", "ABC") == "ABC"
    assert gcd_string("ABCDEFG", "ABCDEFG") == "ABCDEFG"