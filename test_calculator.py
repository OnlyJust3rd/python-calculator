import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-6, -3), -9)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(69, 69), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(11, 11), 121)
        self.assertEqual(self.calc.multiply(6, -9), -54)

    def test_divide(self):
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 10, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertRaises(ZeroDivisionError, self.calc.modulo, 10, 0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()