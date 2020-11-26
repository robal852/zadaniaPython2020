from Zestawy_Zaliczone.zestaw6.points import Point
import unittest


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.zero = 0
        self.one = 1
        self.p0 = Point(0, 0)
        self.p12 = Point(1, 2)
        self.p11 = Point(1, 1)
        self.p22 = Point(2, 2)
        self.p34 = Point(3, 4)
        self.m11 = Point(-1, -1)
        self.p11string = "(1, 1)"
        self.p11repr = "Point(1, 1)"

    def test__init__(self):
        self.assertIsInstance(self.p12, Point)
        self.assertEqual(self.p34.x, 3)
        self.assertEqual(self.p34.y, 4)

    def test__str__(self):
        self.assertEqual(self.p11string, str(self.p11))

    def test__repr__(self):
        self.assertEqual(self.p11repr, repr(self.p11))

    def test__eq__(self):
        self.assertFalse(self.p34 == self.p22, msg="p1 != p2")
        self.assertTrue(self.p34 == self.p34, msg="p1 == p2")

    def test__ne__(self):
        self.assertTrue(self.p34 != self.p22, msg="p1 != p2")
        self.assertFalse(self.p34 != self.p34, msg="p1 == p2")

    def test__add__(self):
        self.assertEqual(self.p0, self.p0 + self.p0, msg="0 + 0")
        self.assertEqual(self.p11, self.p0 + self.p11, msg="0 + 1")
        self.assertEqual(self.p0, self.p11 + self.m11, msg="1 + -1")

    def test__sub__(self):
        self.assertEqual(self.p0, self.p0 - self.p0, msg="0 - 0")
        self.assertEqual(self.m11, self.p0 - self.p11, msg="0 - 1")
        self.assertEqual(self.p22, self.p11 - self.m11, msg="1 - -1")

    def test__mul__(self):
        self.assertEqual(self.zero, self.p0 * self.p0, msg="0 * 0")
        self.assertEqual(14, self.p22 * self.p34, msg="V1 * V2")
        self.assertEqual(-2, self.p11 * self.m11, msg="V1 * V2 <0")

    def test_cross(self):
        self.assertEqual(self.zero, self.p0.cross(self.p0), msg="V1 x V1")
        self.assertEqual(self.zero, self.p11.cross(self.p22), msg="V1 x V2 eq0")
        self.assertEqual(self.one, self.p11.cross(self.p12), msg="V1 x V2")
        self.assertEqual(self.zero, self.p11.cross(self.m11), msg="V1 x -V1")

    def test_length(self):
        self.assertEqual(self.zero, self.p0.length(), msg="length 0")
        self.assertEqual(5, self.p34.length(), msg="length > 0")

    def tearDown(self): pass
