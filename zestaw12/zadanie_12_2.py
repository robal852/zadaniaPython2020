# ZADANIE 12.2 (WYSZUKIWANIE BINARNE)
# Napisać wersję rekurencyjną wyszukiwania binarnego.

def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if left > right:
        print("Nie znaleziono ", y, " w ", L)
        return None
    p = (left + right) // 2
    if L[p] == y:
        return p
    if y < L[p]:
        return binarne_rek(L, left, p - 1, y)
    else:
        return binarne_rek(L, p + 1, right, y)


import numpy as np

size = 11
L = np.random.choice(size, size, replace=True)
L.sort()

print(binarne_rek(L, 0, size - 1, 3))
