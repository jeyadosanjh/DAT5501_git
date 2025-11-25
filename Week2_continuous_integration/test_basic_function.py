import unittest
from basic_function import increment

class unit_tests(unittest.TestCase):

    def test_increment_positive(self):
        self.assertEqual(increment(5), 6)

    def test_increment_negative(self):
        self.assertEqual(increment(-3), -2)

    def test_increment_zero(self):
        self.assertEqual(increment(0), 1)

    def test_increment_non_number(self):
        with self.assertRaises(TypeError):
            increment("a string")

if __name__ == '__main__':
    unittest.main()
