import math


def solve2(a, b, c):
    """Rozwiązywanie równania kwadratowego a * x * x + b * x + c = 0."""
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
    elif delta == 0:
        x1 = -b / 2 * a
        x2 = x1
    else:
        delta = math.sqrt(-delta)
        x1 = complex(-b / (2 * a), -delta / (2 * a))
        x2 = complex(-b / (2 * a), delta / (2 * a))
    return ([x1, x2])


import unittest


class Testzadanie_8_2(unittest.TestCase):
    def testsolve2(self):
        self.assertEqual(solve2(1, 4, 3), [-3.0, -1.0])
        self.assertEqual(solve2(1, -4, 4), [2.0, 2.0])
        self.assertEqual(solve2(1, 1, 1), [(-0.5 - 0.8660254037844386j), (-0.5 + 0.8660254037844386j)])
