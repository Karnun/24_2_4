import unittest
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator().add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(Calculator().subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(Calculator().multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(Calculator().divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()
