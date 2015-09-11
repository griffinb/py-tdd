import unittest
from calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(6, self.calc.add(3, 3))

    def test_add_method_raises_typeerror_if_not_ints(self):
         self.assertRaises(TypeError, self.calc.add, "Hello", "World")

    def test_error(self):
        with self.assertRaises(AttributeError):
            self.calc.subtract(7, 5)

    def test_assert_equal(self):
        self.assertEqual(1, 1)

    def test_assert_raises(self):
        self.assertRaises(ValueError, int, "a")

    def test_assert_raises_alternative(self):
        with self.assertRaises(AttributeError):
            [].get

    def test_assert_greater(self):
        self.assertGreater(2, 1, "Value is not greater.")

    def test_assert_in(self):
        self.assertIn(1, (1, 2, 3))

if __name__ == '__main__':
    unittest.main()