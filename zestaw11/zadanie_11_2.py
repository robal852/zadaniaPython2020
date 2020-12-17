from zestaw11.listy import *


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów na liście."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item


def shakersort(L, left, right):
    k = right
    while left < right:
        for j in range(right, left, -1):
            if L[j - 1] > L[j]:
                swap(L, j - 1, j)
                zapiszDoPliku(L)
                k = j
        left = k
        for j in range(left, right):
            if L[j] > L[j + 1]:
                swap(L, j, j + 1)
                zapiszDoPliku(L)
                k = j
        right = k


def zapiszDoPliku(L, filename="sort1.dat"):
    f = open(filename, "w")
    for i in range(len(L)):
        f.write(str(i)+" "+ str(L[i])+"\n")
    f.close()


size = 1000
l1 = intLosowe(size)
l2 = intLosowePrawwiePosortowane(size)
l3 = intOdwrotnaKolejnosc(size)
l4 = floatGaussa(size)
l5 = int_z_powtorzeniami(size)



zapiszDoPliku(l1)