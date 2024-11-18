import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_1(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_2(self):
        self.assertEqual(self.calc.add(-3, -2), -5)  # -3 + (-2) = -5

    # Tests for subtract
    def test_subtract_1(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)  # 5 - 3 = 2

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)  # 3 - 5 = -2

    # Tests for multiply
    def test_multiply_1(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)  # 2 * 3 = 6

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)  # 5 * 0 = 0

    # Tests for divide
    def test_divide_1(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  # 10 / 2 = 5

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(7, 2), 3)  # 7 // 2 = 3 (integer division)

    # Tests for modulo
    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)  # 10 % 2 = 0

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)  # 10 % 3 = 1

if __name__ == '__main__':
    unittest.main()