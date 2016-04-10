import unittest
from stackfuck.token import Token

class TestToken(unittest.TestCase):

    def test_constructor_no_kwargs(self):
        self.assertRaises(AssertionError, Token)

    def test_constructor_wrong_kwargs(self):
        self.assertRaises(AssertionError, Token, type="foo") # missing value
        self.assertRaises(AssertionError, Token, value="bar") # missing type

    def test_constructor(self):
        token = Token(type="foo", value="bar")
        self.assertEqual(token.type, "foo")
        self.assertEqual(token.value, "bar")

    def test_constructor_with_misc_kwargs(self):
        token = Token(type="foo", value="bar", body="baz")
        self.assertEqual(token.body, "baz")


if __name__ == '__main__':
    unittest.main()
