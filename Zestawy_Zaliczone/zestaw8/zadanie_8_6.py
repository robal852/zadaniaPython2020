# Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j).
# Porównać z wersją rekurencyjną programu.
# Wskazówka: Wykorzystać tablicę dwuwymiarową (np. słownik) do przechowywania wartości funkcji.
# Wartości w tablicy wypełniać kolejno wierszami.
# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.


# P(wiersz, kolumna)
def P(i, j):
    if i < 0 or j < 0:
        raise ValueError("Podano ujemne wartosci!")
    P = [[0 for k in range(j + 1)]
         for w in range(i + 1)]

    for w in range(i + 1):
        for k in range(j + 1):
            if w == 0 and k == 0:
                P[w][k] = 0.5
            elif w > 0 and k == 0:
                P[w][k] = 0.0
            elif w == 0 and k > 0:
                P[w][k] = 1.0
            else:
                P[w][k] = 0.5 * (P[w - 1][k] + P[w][k - 1])
    return P[i][j]


# [[0.5        1.         1.         1.         1.         1.         1.        ]
# [0.         0.5        0.75       0.875      0.9375     0.96875    0.984375  ]
# [0.         0.25       0.5        0.6875     0.8125     0.890625   0.9375    ]
# [0.         0.125      0.3125     0.5        0.65625    0.7734375  0.85546875]
# [0.         0.0625     0.1875     0.34375    0.5        0.63671875 0.74609375]
# [0.         0.03125    0.109375   0.2265625  0.36328125 0.5        0.62304688]
# [0.         0.015625   0.0625     0.14453125 0.25390625 0.37695312 0.5       ]]

import unittest


class Testzadanie_8_6(unittest.TestCase):

    def testP(self):
        self.assertEqual(0.5, P(2, 2))
        self.assertEqual(0, P(3, 0))
        self.assertEqual(1, P(0, 3))

        try:
            P(-1, 0)
        except Exception as ex:
            self.assertEqual(ValueError, ex.__class__)
