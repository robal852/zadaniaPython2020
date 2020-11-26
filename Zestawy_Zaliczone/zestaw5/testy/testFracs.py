from Zestawy_Zaliczone.zestaw5.fracs import *

import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(self.zero, add_frac([-1, 2], [1, 2]))

    def test_sub_frac(self):
        self.assertEqual([-1, 2], sub_frac([-1, 2], self.zero), msg="Blad w odejowaniu")
        self.assertEqual(self.zero, sub_frac([3, 1], [6, 2]), msg="Blad w odejowaniu")
        self.assertEqual(self.zero, sub_frac([-1, 2], [-1, 2]), msg="Blad w odejowaniu")
        self.assertEqual([-3, 1], sub_frac(self.zero, [3, 1]), msg="Blad w odejowaniu")

    def test_mul_frac(self):
        self.assertEqual(self.zero, mul_frac([0, 5], [9, 1]), "mnozenie przez zero")
        self.assertEqual([1, 4], mul_frac([1, 2], [1, 2]))

    def test_div_frac(self):
        self.assertEqual([1, 1], div_frac([1, 2], [1, 2]))
        self.assertEqual([25, 4], div_frac([5, 2], [2, 5]))
        self.assertEqual([2, 1], div_frac([10, 1], [25, 5]))
        self.assertEqual([1, 2], div_frac([1, 4], [1, 2]))

    def test_is_positive(self):
        self.assertEqual(True, is_positive([1, 2]))
        self.assertEqual(False, is_positive([-1, 2]))

    def test_is_zero(self):
        self.assertEqual(True, is_zero(self.zero))
        self.assertEqual(False, is_zero([1, 5]))

    def test_cmp_frac(self):
        self.assertEqual(0, cmp_frac([0, 5], [0, 19]))
        self.assertEqual(1, cmp_frac([1, 5], [-1, 5]))
        self.assertEqual(-1, cmp_frac([1, 5], [1, 2]))

    def test_frac2float(self):
        self.assertEqual(0.5, frac2float([1, 2]))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
