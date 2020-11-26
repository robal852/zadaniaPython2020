from Zestawy_Zaliczone.zestaw6.points import Point


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        ''' "[(x1, y1), (x2, y2), (x3, y3)]" '''
        return "[" + str(self.pt1) + ", " + str(self.pt2) + ", " + str(self.pt3) + "]"

    def __repr__(self):
        ''' "Triangle(x1, y1, x2, y2, x3, y3)" '''
        return "Triangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(
            self.pt2.y) + ", " + str(self.pt3.x) + ", " + str(self.pt3.y) + ")"

    def __eq__(self, other):
        ''' obsługa tr1 == tr2 '''
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

    def __ne__(self, other):  # obsługa tr1 != tr2
        return not self == other

    def center(self):
        ''' zwraca środek trójkąta '''
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):
        ''' pole powierzchni '''
        return self.pt1.cross(self.pt2) / 2

    def move(self, x, y):
        ''' przesunięcie o (x, y) '''
        return Triangle(self.pt1.x + x, self.pt1.y + y,
                        self.pt2.x + x, self.pt2.y + y,
                        self.pt3.x + x, self.pt3.y + y)
