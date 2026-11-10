import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # --- add() ---
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    # --- subtract() ---
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-1, -2), 1)

    # --- multiply() ---
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(3, -2), -6)

    # --- divide() ---
    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-6, 2), -3)

    # --- modulo() ---
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_zero_remainder(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)

if __name__ == '__main__':
    unittest.main()
