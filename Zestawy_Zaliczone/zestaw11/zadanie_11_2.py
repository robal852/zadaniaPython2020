# INSTRUKCJA
# Pracuję z Ubuntu i najpierw uruchamiam "podgladSortowania" w podstawowej aplikacji "Obrazy"
# następnie uruchamiam skrypt z sortowaniem
# W czasie działania skryptu zmienia sie obrazek i widzę co dziee się na liście.
# Jeśli, nie zdąży się wczytywać nowy obrazek, można powiekszyc zmienna delay

# Mozna też odkomentować linijke     #os.system("display podgladSortowania"),
# wtedy widzimy kazdy krok przez ile chcemy czasu, a następny dopiero po zamknięciu okna z wczesniejszym


import os
import time

from Zestawy_Zaliczone.zestaw11.listy import *

delay = 0.42


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
        f.write(str(i) + " " + str(L[i]) + "\n")
    f.close()
    os.system("gnuplot podglad.gp")
    # os.system("display podgladSortowania")
    time.sleep(delay)


size = 16
l1 = intLosowe(size)
l2 = intLosowePrawwiePosortowane(size)
l3 = intOdwrotnaKolejnosc(size)
l4 = floatGaussa(size)
l5 = int_z_powtorzeniami(size)

shakersort(l1, 0, size - 1)
shakersort(l2, 0, size - 1)
shakersort(l3, 0, size - 1)
shakersort(l4, 0, size - 1)
shakersort(l5, 0, size - 1)
