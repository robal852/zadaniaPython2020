from Zestawy_Zaliczone.zestaw7.fracs import Frac
import unittest


class TestFrac(unittest.TestCase):

    def setUp(self):
        self.zero = Frac(0, 1)
        self.one = Frac(1, 1)
        self.fl = Frac(1.0, 0.5)
        self.f1 = Frac(1.5, 2)
        self.f2 = Frac(2, 0.5)
        self.f4 = Frac(4, 1)
        self.f12 = Frac(1, 2)
        self.f34 = Frac(3, 4)

    def test__init__(self):
        self.assertIsInstance(self.zero, Frac)
        self.assertIsInstance(self.f1, Frac)
        self.assertIsInstance(self.f2, Frac)
        self.assertIsInstance(self.fl, Frac)
        try:
            Frac(1, 0)
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)
        self.assertEqual(0, self.zero.x)
        self.assertEqual(1, self.zero.y)
        self.assertEqual(2, self.fl.x)
        self.assertEqual(1, self.fl.y)

    def test__str__(self):
        self.assertEqual('2', str(self.fl))
        self.assertEqual('1/2', str(self.f12))

    def test__repr__(self):
        self.assertEqual('Frac(2, 1)', repr(self.fl))

    def test__eq__(self):
        self.assertFalse(self.zero == self.f12)
        self.assertTrue(self.f4 == self.f2)
        self.assertTrue(self.f12 == 0.5)

    def test__ne__(self):
        self.assertTrue(self.zero != self.f12)
        self.assertFalse(self.f4 != self.f2)

    def test__lt__(self):
        self.assertTrue(self.zero < self.f4)
        self.assertFalse(self.f4 < self.zero)

    def test__le__(self):
        self.assertTrue(self.zero <= self.f4)
        self.assertTrue(self.f4 <= self.f4)
        self.assertFalse(self.f4 <= self.zero)

    def test__add__(self):
        self.assertEqual(Frac(5, 4), self.f12 + self.f34)
        self.assertEqual(self.one, self.f12 + self.f12)
        self.assertEqual(self.one, self.f12 + 0.5)
        self.assertEqual(self.one, self.zero + 1)

    def test__radd__(self):
        self.assertEqual(self.one, 1 + self.zero)
        self.assertEqual(Frac(3, 2), 1 + self.f12)

    def test__sub__(self):
        self.assertEqual(Frac(-1, 4), self.f12 - self.f34)
        self.assertEqual(self.zero, self.f12 - self.f12)
        self.assertEqual(self.f12, self.f12 - 0)
        self.assertEqual(Frac(-1, 1), self.zero - 1)

    def test__rsub__(self):
        self.assertEqual(self.one, 1 - self.zero)
        self.assertEqual(self.zero, 1 - self.one)
        self.assertEqual(self.zero, 0.5 - self.f12)
        self.assertEqual(self.one, 1.5 - self.f12)

    def test__mul__(self):
        self.assertEqual(self.zero, self.f12 * self.zero)
        self.assertEqual(self.one, self.f12 * 2)

    def test__rmul__(self):
        self.assertEqual(self.zero, 0 * self.f12)
        self.assertEqual(self.one, 2 * self.f12)

    def test__truediv__(self):
        try:
            self.f12 / self.zero
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)
        try:
            self.f12 / 0
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)
        self.assertEqual(self.one, self.f12 / self.f12)
        self.assertEqual(self.one, self.one / 1)

    def test__rtruediv__(self):
        self.assertEqual(self.one, self.one.__rtruediv__(1))
        self.assertEqual(self.f4, 2 / self.f12)

    def test__pos__(self):
        self.assertEqual(self.f12, +self.f12)

    def test__neg__(self):
        self.assertEqual(Frac(-1, 2), -self.f12)

    def test__invert__(self):
        self.assertEqual(Frac(2, 1), self.f12.__invert__())

    def test__float__(self):
        self.assertEqual(0.5, self.f12.__float__())

    def test__hash__(self):
        self.assertEqual(hash(0.5), self.f12.__hash__())

    def tearDown(self):
        pass
