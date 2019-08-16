import unittest
from fizzbuzz import fizzbuzz
from nose.tools import eq_

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        res = ['1']
        eq_(fizzbuzz(1), res)

        res = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", 
            "11","Fizz", "13", "14", "FizzBuzz"
        ]
        eq_(fizzbuzz(15), res)

if __name__ == "__main__":
    unittest.main()
