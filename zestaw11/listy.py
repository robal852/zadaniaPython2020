# Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. Przydatne są m.in. następujące rodzaje danych:
# (a) różne liczby int od 0 do N-1 w kolejności losowej,
# (b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N).


import random
import numpy as np

def intLosowe(size):
    l = list(range(0, size))
    random.shuffle(l)
    return l

def intLosowePrawwiePosortowane(size): #mieszam tylko w zakresie kolejnych pieciu liczb
    l = list(range(0, size))
    l = [l[i:i + 5] for i in range(0, len(l), 5)]
    #print(l)
    for i in l:
        random.shuffle(i)
    #print(l)
    l = [j for i in l for j in i]
    return l

def intOdwrotnaKolejnosc(size):
    l = list(range(0, size))
    l.reverse()
    return l

def floatGaussa(size):
    mu, sigma = 0, 1
    l = np.random.normal(mu, sigma, size)
    return l

def int_z_powtorzeniami(size):
    l = np.random.choice(size, size, replace=True)
    return l


if __name__ == "__main__":
    print("a")
    print(intLosowe(15))

    print("b)")
    print(intLosowePrawwiePosortowane(16))

    print("c)")
    print(intOdwrotnaKolejnosc(15))

    print("d)")
    print(floatGaussa(10))

    print("e)")
    print(int_z_powtorzeniami(11))