from unittest import TestCase

from ddt import data
from ddt import ddt
from ddt import unpack

from proj.foo import divide


@ddt
class TestFoo(TestCase):
    @data(
        (6, 2, 3.0),
        (6, -2, -3.0),
        (-6, 2, -3.0),
        (-6, -2, 3.0),
        (9, 4, 2.25),
        (0, 2, 0),
        (0, -2, 0),
        (-0, 2, 0),
        (-0, -2, 0),
    )
    @unpack
    def test_divide_valid(self, n: float, d: float, r: float) -> None:
        self.assertAlmostEqual(divide(n, d), r)

    @data(
        (6, 0),
        (6, -0),
        (0, 0),
        (0, -0),
        (-0, 0),
        (-0, -0),
    )
    @unpack
    def test_divide_invalid(self, n: float, d: float) -> None:
        with self.assertRaises(ZeroDivisionError):
            divide(n, d)
