"""Run with: python -m unittest discover -s tests -v"""

import contextlib
import io
import unittest

from equations import main, solve_linear, solve_quadratic


class EquationTests(unittest.TestCase):
    def test_linear_equation(self):
        self.assertEqual(solve_linear(2, -6), 3)
        self.assertEqual(solve_linear(-4, -8), -2)

    def test_linear_requires_nonzero_coefficient(self):
        with self.assertRaises(ValueError):
            solve_linear(0, 5)

    def test_quadratic_two_real_roots(self):
        self.assertEqual(solve_quadratic(1, -3, 2), (1, 2))
        self.assertEqual(solve_quadratic(-1, 0, 4), (-2, 2))

    def test_quadratic_repeated_root(self):
        self.assertEqual(solve_quadratic(1, -2, 1), (1,))

    def test_quadratic_no_real_roots(self):
        self.assertEqual(solve_quadratic(1, 0, 1), ())

    def test_quadratic_requires_nonzero_leading_coefficient(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, -6)

    def test_command_line_output(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(main(["quadratic", "1", "-3", "2"]), 0)
        self.assertEqual(output.getvalue(), "x = 1\nx = 2\n")


if __name__ == "__main__":
    unittest.main()
