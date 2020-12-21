# ZADANIE 12.3 (MEDIANA)
# Zaimplementować prostą metodę znajdowania mediany polegającą na posortowaniu zbioru i wybraniu elementu środkowego.

def mediana_sort(L, left, right):
    L.sort()
    if len(L) % 2:
        i = ((left + right) // 2)
        return L[i]
    else:
        i = (left + right) // 2
        return (L[i] + L[i + 1]) / 2


L = [0, 1, 2, 3, 4, 5]
print(mediana_sort(L, 0, len(L) - 1))
L = [100, 50]
print(mediana_sort(L, 0, len(L) - 1))
