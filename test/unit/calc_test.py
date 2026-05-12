import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator, InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # -------------------------
    # ADD
    # -------------------------

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    # -------------------------
    # SUBSTRACT
    # -------------------------

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)

    # -------------------------
    # MULTIPLY
    # -------------------------

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_fails_with_nan_parameter(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)

    def test_multiply_method_fails_with_invalid_permissions(self):
        with patch('app.util.validate_permissions', return_value=False, create=True):
            self.assertRaises(InvalidPermissions, self.calc.multiply, 2, 2)

    # -------------------------
    # DIVIDE
    # -------------------------

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    # -------------------------
    # POWER
    # -------------------------

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(1, self.calc.power(2, 0))
        self.assertEqual(0.25, self.calc.power(2, -2))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")

    # -------------------------
    # SQUARE ROOT
    # -------------------------

    def test_square_root_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.square_root(4))
        self.assertEqual(3, self.calc.square_root(9))
        self.assertEqual(0, self.calc.square_root(0))

    def test_square_root_method_fails_with_invalid_parameter(self):
        self.assertRaises(TypeError, self.calc.square_root, "4")
        self.assertRaises(TypeError, self.calc.square_root, None)
        self.assertRaises(TypeError, self.calc.square_root, -4)

    # -------------------------
    # LOGARITHM
    # -------------------------

    def test_logarithm_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.logarithm(10))
        self.assertEqual(2, self.calc.logarithm(100))
        self.assertEqual(0, self.calc.logarithm(1))

    def test_logarithm_method_fails_with_invalid_parameter(self):
        self.assertRaises(TypeError, self.calc.logarithm, "10")
        self.assertRaises(TypeError, self.calc.logarithm, None)
        self.assertRaises(TypeError, self.calc.logarithm, 0)
        self.assertRaises(TypeError, self.calc.logarithm, -10)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()