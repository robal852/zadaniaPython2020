# Zaimplementować algorytm obliczający pole powierzchni trójkąta,
# jeżeli dane są trzy liczby będące długościami jego boków.
# Jeżeli podane liczby nie spełniają warunku trójkąta,
# to program ma generować wyjątek ValueError.
import math


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        return (math.sqrt(p * (p - a) * (p - b) * (p - c)))
    else:
        raise ValueError("Nie spełniony warunek trójkąta!")


import unittest


class Testzadanie_8_4(unittest.TestCase):

    def testheron(self):
        self.assertEqual(6, heron(3, 4, 5))

        try:
            heron(100, 50, 5)
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)
