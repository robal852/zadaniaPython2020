from zestaw6.triangles import Triangle
from zestaw6.points import Point
import unittest


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.zero = 0
        self.one = 1
        self.t1 = Triangle(1, 0, 0, 1, 1, 1)
        self.t2 = Triangle(2, 0, 0, 2, 2, 2)
        self.t3 = Triangle(2, 2, 2, 0, 0, 2)
        self.t4 = Triangle(3, 4, 3, 2, 1, 4)

        self.p1 = Point(1, 0)
        self.p2 = Point(0, 1)
        self.p3 = Point(1, 1)
        self.t1string = "[(1, 0), (0, 1), (1, 1)]"
        self.t1repr = "Triangle(1, 0, 0, 1, 1, 1)"
        self.ctr1 = Point(2 / 3, 2 / 3)
        self.area1 = 0.5

    def test__init__(self):
        self.assertIsInstance(self.t1, Triangle)
        self.assertEqual(self.t1.pt1, self.p1)
        self.assertEqual(self.t1.pt2, self.p2)
        self.assertEqual(self.t1.pt3, self.p3)

    def test__str__(self):
        self.assertEqual(self.t1string, str(self.t1))

    def test__repr__(self):
        self.assertEqual(self.t1repr, repr(self.t1))

    def test__eq__(self):
        self.assertFalse(self.t1 == self.t2, msg="t1 != t2")
        self.assertTrue(self.t2 == self.t2, msg="t1 == t2")
        self.assertTrue(self.t2 == self.t3, msg="t1, t3 other order")

    def test__ne__(self):
        self.assertTrue(self.t1 != self.t2, msg="t1 != t2")
        self.assertFalse(self.t2 != self.t3, msg="t1 == t2")

    def test_center(self):
        self.assertEqual(self.ctr1, self.t1.center())

    def test_area(self):
        self.assertEqual(self.area1, self.t1.area())

    def test_move(self):
        self.assertEqual(self.t4, self.t3.move(1, 2), msg="move(1, 2)")
        self.assertEqual(self.t3, self.t4.move(-1, -2), msg="move(-1, -2)")

    def tearDown(self): pass
