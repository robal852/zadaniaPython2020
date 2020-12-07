import unittest

from Zestawy_Zaliczone.zestaw6.points import Point
from Zestawy_Zaliczone.zestaw7.triangles import Triangle


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.t1 = Triangle(0, 0, 2, 0, 0, 2)
        self.t2 = Triangle(2, 2, 2, 0, 0, 2)
        self.t3 = Triangle(0, 3, 1, 0, 2, 3)
        self.t4 = Triangle(2, 3, 0, 3, 1, 0)
        self.t3center = Point(1, 2)
        self.t3mv = Triangle(1, 4, 2, 1, 3, 4)

    def test__init__(self):
        self.assertIsInstance(self.t1, Triangle)
        try:
            Triangle(1, 1, 2, 1, 3, 1)
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)

        try:
            Triangle(0, 0, 1, 0, 2, 0)
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)

        try:
            Triangle(1, 1, 1, 1, 1, 1)
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)

    def test__str__(self):
        self.assertEqual("[(0, 0), (2, 0), (0, 2)]", str(self.t1))

    def test__repr__(self):
        self.assertEqual("Triangle(0, 0, 2, 0, 0, 2)", repr(self.t1))

    def test__eq__(self):
        self.assertFalse(self.t1 == self.t2)
        self.assertTrue(self.t1 == self.t1)
        self.assertTrue(self.t3 == self.t4)

    def test__ne__(self):
        self.assertTrue(self.t1 != self.t2)
        self.assertFalse(self.t1 != self.t1)

    def testcenter(self):
        self.assertEqual(self.t3center, self.t3.center())

    def testarea(self):
        self.assertEqual(2, self.t1.area())
        self.assertEqual(2, self.t2.area())

    def testmove(self):
        self.assertEqual(self.t3mv, self.t3.move(1, 1))
        self.assertEqual(self.t3, self.t3mv.move(-1, -1))

    def testmake4(self):
        self.assertEqual([Triangle(1.0, 0.0, 0.0, 1.0, 1.0, 1.0), Triangle(0, 0, 1.0, 0.0, 0.0, 1.0),
                          Triangle(2, 0, 1.0, 0.0, 1.0, 1.0), Triangle(0, 2, 0.0, 1.0, 1.0, 1.0)], self.t1.make4() )

        def tearDown(self):
            pass
