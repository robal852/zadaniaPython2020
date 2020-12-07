import math

from Zestawy_Zaliczone.zestaw6.points import Point


def distance(x1, y1, x2, y2):
    '''Distance between two points'''
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)


class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        if ((abs(distance(x1, y1, x2, y2) - distance(x2, y2, x3, y3)) < distance(x1, y1, x3, y3)) and (abs(
                distance(x1, y1, x3, y3) < (
                        distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3))))):  # ||AB|-|BC||<|AC|<|AB|+|BC|.
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
            self.pt3 = Point(x3, y3)
        else:
            raise ValueError("punkty sa wspoliniowe")

    def __str__(self):
        '''"[(x1, y1), (x2, y2), (x3, y3)]"'''
        return "[" + str(self.pt1) + ", " + str(self.pt2) + ", " + str(self.pt3) + "]"

    def __repr__(self):
        '''"Triangle(x1, y1, x2, y2, x3, y3)"'''
        return "Triangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(
            self.pt2.y) + ", " + str(self.pt3.x) + ", " + str(self.pt3.y) + ")"

    def __eq__(self, other):  # zakładam, że jak ma wierzchołki w innej kolejności to jest różny
        '''obsługa tr1 == tr2'''
        if self.pt1 == other.pt1:
            if self.pt2 == other.pt2 and self.pt3 == other.pt3:
                return True
            if self.pt2 == other.pt3 and self.pt3 == other.pt2:
                return True
        if self.pt1 == other.pt2:
            if self.pt2 == other.pt1 and self.pt3 == other.pt3:
                return True
            if self.pt2 == other.pt3 and self.pt3 == other.pt1:
                return True
        if self.pt1 == other.pt3:
            if self.pt2 == other.pt1 and self.pt3 == other.pt2:
                return True
            if self.pt2 == other.pt2 and self.pt3 == other.pt1:
                return True
        return False

    def __ne__(self, other):
        '''obsługa tr1 != tr2'''
        return not self == other

    def center(self):
        '''zwraca środek ciężkości trójkąta'''
        x = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        y = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(x, y)

    def area(self):
        '''pole powierzchni'''
        return 0.5 * distance(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y) * distance(self.pt1.x, self.pt1.y,
                                                                                         self.pt3.x,
                                                                                         self.pt3.y)

    def move(self, x, y):
        ''' przesunięcie o (x, y) '''
        return (
            Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y, self.pt3.x + x, self.pt3.y + y))

    def make4(self):
        '''zwraca krotkę czterech mniejszych'''
        sx1 = 0.5 * (self.pt1.x + self.pt2.x)
        sy1 = 0.5 * (self.pt1.y + self.pt2.y)
        sx2 = 0.5 * (self.pt1.x + self.pt3.x)
        sy2 = 0.5 * (self.pt1.y + self.pt3.y)
        sx3 = 0.5 * (self.pt2.x + self.pt3.x)
        sy3 = 0.5 * (self.pt2.y + self.pt3.y)
        t1 = Triangle(sx1, sy1, sx2, sy2, sx3, sy3)
        t2 = Triangle(self.pt1.x, self.pt1.y, sx1, sy1, sx2, sy2)
        t3 = Triangle(self.pt2.x, self.pt2.y, sx1, sy1, sx3, sy3)
        t4 = Triangle(self.pt3.x, self.pt3.y, sx2, sy2, sx3, sy3)
        return [t1, t2, t3, t4]
