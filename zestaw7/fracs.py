import math


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x, y):
        # Sprawdzamy, czy y=0.
        if y == 0:
            raise ValueError
        if isinstance(x, float):
            if isinstance(y, float):
                self.x = x.as_integer_ratio()[0] * y.as_integer_ratio()[1]
                self.y = x.as_integer_ratio()[1] * y.as_integer_ratio()[0]
            if isinstance(y, int):
                self.x = x.as_integer_ratio()[0]
                self.y = x.as_integer_ratio()[1] * y
        elif isinstance(x, int) and isinstance(y, float):
            self.x = y.as_integer_ratio()[1] * x
            self.y = y.as_integer_ratio()[0]
        else:
            self.x = x
            self.y = y

    def __str__(self):
        ''' zwraca "x/y" lub "x" dla y=1 '''
        if self.y == 1:
            return str(self.x)
        return str(self.x) + "/" + str(self.y)

    def __repr__(self):
        ''' zwraca "Frac(x, y)" '''
        return "Frac(" + str(self.x) + ", " + str(self.y) + ")"

    # Python 2
    # def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        if isinstance(other, Frac):
            if self.x == other.x and self.y == other.y:
                return True
            return False
        elif isinstance(other, int):
            if self.x == other and self.y == 1:
                return True
            else:
                return False
        else:
            raise ValueError

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    # def __gt__(self, other): pass

    # def __ge__(self, other): pass

    def __add__(self, other):
        ''' frac1+frac2, frac+int '''
        if isinstance(other, Frac):
            nominator = self.x * other.y + self.y * other.x
            denominator = self.y * other.y
        elif isinstance(other, int):
            nominator = self.x + other * self.y
            denominator = self.y
        elif isinstance(other, float):
            otherX, otherY = other.as_integer_ratio()
            nominator = self.x * otherY + self.y * otherX
            denominator = self.y * otherY
        else:
            raise ValueError
        gcd = math.gcd(nominator, denominator)
        return Frac(nominator / gcd, denominator / gcd)

    __radd__ = __add__  # int+frac

    def __sub__(self, other):
        ''' frac1-frac2, frac-int'''
        if isinstance(other, Frac):
            nominator = self.x * other.y - self.y * other.x
            denominator = self.y * other.y
        elif isinstance(other, int):
            nominator = self.x - other * self.y
            denominator = self.y
        elif isinstance(other, float):
            otherX, otherY = other.as_integer_ratio()
            nominator = self.x * otherY - self.y * otherX
            denominator = self.y * otherY
        else:
            raise ValueError
        gcd = math.gcd(nominator, denominator)
        return Frac(nominator / gcd, denominator / gcd)

    def __rsub__(self, other):  # int-frac
        ''' tutaj self jest frac, a other jest int! '''
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        ''' frac1*frac2, frac*int '''
        if isinstance(other, Frac):
            nominator = self.x * other.x
            denominator = self.y * other.y
        elif isinstance(other, int):
            nominator = self.x * other
            denominator = self.y
        else:
            raise ValueError
        gcd = math.gcd(nominator, denominator)
        return Frac(nominator / gcd, denominator / gcd)

    __rmul__ = __mul__  # int*frac

    # def __div__(self, other):
    #     pass  # frac1/frac2, frac/int, Python 2
    #
    # def __rdiv__(self, other):
    #     pass  # int/frac, Python 2

    def __truediv__(self, other):
        ''' frac1/frac2, frac/int, Python 3 '''
        if isinstance(other, Frac):
            if other.x == 0:
                raise ValueError
            nominator = self.x * other.y
            denominator = self.y * other.x
        elif isinstance(other, int):
            if other == 0:
                raise ValueError
            nominator = self.x
            denominator = self.y * other
        else:
            raise ValueError
        gcd = math.gcd(nominator, denominator)
        return Frac(nominator / gcd, denominator / gcd)

    def __rtruediv__(self, other):
        ''' int/frac, Python 3 '''
        if isinstance(other, Frac):
            nominator = self * other.y
            denominator = other.x
            gcd = math.gcd(nominator, denominator)
            return Frac(nominator / gcd, denominator / gcd)

    # operatory jednoargumentowe
    def __pos__(self):
        ''' +frac = (+1)*frac '''
        return self

    def __neg__(self):
        ''' -frac = (-1)*frac '''
        return Frac(-self.x, self.y)

    def __invert__(self):
        ''' odwrotnosc: ~frac '''
        return Frac(self.y, self.x)

    def __float__(self):
        ''' float(frac) '''
        return float(self.x / self.y)

    def __hash__(self):
        return hash(float(self))  # immutable fracs
        # assert set([2]) == set([2.0])
