import unittest
from legmath import fabsmax
from legmath import roundsig


class TestLegMath(unittest.TestCase):

    def test_roundisg(self):
        self.assertAlmostEqual(roundsig(114.525, 3), 115.0, 3)
        self.assertAlmostEqual(roundsig(14.525, 3), 14.5, 3)
        self.assertAlmostEqual(roundsig(4.525, 3), 4.53, 3)
        self.assertAlmostEqual(roundsig(-4.525, 3), -4.53, 3)

    def test_fabsmax(self):
        # Should work with integer
        self.assertEqual(fabsmax([1, 2, 3, -4]), 4)
        # and floats
        self.assertAlmostEqual(
            fabsmax([-0.0041234, 2.431, -7.542, -3.9922]), 7.542, 3)
        # and both at the same time, here with float winning
        self.assertAlmostEqual(
            fabsmax([-0.0041234, 1, -7.542, -3.9922]), 7.542, 3)
        # and here with decimal winning
        self.assertAlmostEqual(
            fabsmax([-0.0041234, 15, -7.542, -3.9922]), 15, 3)
