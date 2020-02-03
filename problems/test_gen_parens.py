import unittest
from gen_parens import *
from nose.tools import eq_

class TestGenParens(unittest.TestCase):
    def test_gen_parens(self):
        eq_(set(gen_parens(1)), {'()'})
        eq_(set(gen_parens(2)), {'()()', '(())'})
        eq_(set(gen_parens(3)), {'()(())', '(()())', '((()))', '()()()', '(())()'})

    def test_gen_parens_bf(self):
        eq_(set(gen_parens_bf(1)), {'()'})
        eq_(set(gen_parens_bf(2)), {'()()', '(())'})
        eq_(set(gen_parens_bf(3)), {'()(())', '(()())', '((()))', '()()()', '(())()'})

if __name__ == "__main__":
    unittest.main()