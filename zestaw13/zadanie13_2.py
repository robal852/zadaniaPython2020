# Zbadać problem hetmanów dla różnych rozmiarów szachownicy.
# Zmodyfikować program tak, aby znajdował wszystkie rozwiązania problemu hetmanów na szachownicy

# Problem ośmiu hetmanów.
# Wiersze i kolumny mają zakres od 0 do N-1.

def rysuj():
    for w in range(N):
        print ( " ".join(("H" if x[k] == w else ".") for k in range(N)) )
    print("")

def dopuszczalny(w, k):
    return a[w] and b[w+k] and c[w-k]

def zapisz(w, k):
    x[k] = w
    a[w] = False
    b[w+k] = False
    c[w-k] = False

def wymaz(w, k):
    a[w] = True
    b[w+k] = True
    c[w-k] = True

# Znajdowanie jednego rozwiązania.
# def probuj(k):
#     udany = False
#     w = 0                 # numery od 0 do N-1
#     while (not udany) and (w < N):
#         if dopuszczalny(w, k):
#             zapisz(w, k)
#             if k < (N-1):
#                 udany = probuj(k+1)
#                 if not udany:
#                     wymaz(w, k)
#             else:
#                 udany = True
#         w += 1
#     return udany

def probuj(k):
    # Sprawdzanie wszystkich kandydatow (wiersze).
    for w in range(N):
        if dopuszczalny(w, k):
            zapisz(w, k)
            if k < (N-1):
                probuj(k+1)
            else:
                rysuj()
            wymaz(w, k)


N = 8  # bok szachownicy i jednocześnie liczba hetmanów

# x[i] to pozycja hetmana w kolumnie i
x = N * [None]

# a[j] == True to brak hetmana w wierszu j
a = N * [True]

# b[k] == True to brak hetmana na przekątnej k [/].
# Suma wiersz+kolumna od 0 do (2N-2).
b = (2*N-1) * [True]

# c[k] == True to brak hetmana na przekątnej k [\].
# Różnica wiersz-kolumna od (-N+1) do (N-1).
c = (2*N-1) * [True]

if probuj(0):
    print ( "Mamy rozwiązanie" )
    rysuj()
else:
    print ( "Nie istnieje rozwiązanie" )
# Problem ośmiu hetmanów.
# Znajdowanie wszystkich rozwiązań.


# przyklad: dla szachownicy 4x4 mamy dwa rozwiazania
#
# . . H .
# H . . .
# . . . H
# . H . .
#
# . H . .
# . . . H
# H . . .
# . . H .


# natomiast dla szachownicy 5x5 jest to juz 10 rozwiazan, ale jesli uznamy ze mozemy dowolnie obracac szachownice sa to tak na prawde 3 rozwiazania
# takie jak pierwsze i drugie gdzie pozostale to te rozwiazania obrocone w inna strone                   (2x4 rozwiazan)
# oraz czwarte rozwiazanie ale tu obrót szachownicy nie zmienia miejsc zajetych przez hetmany            (1 rozwiazanie)
# rozwiazanie 7. jest lustrzanym odbiciem rozwiazania nr 4                                               (1 rozwiazanie)

#1.
# H . . . .
# . . . H .
# . H . . .
# . . . . H
# . . H . .
#
#2.
# H . . . .
# . . H . .
# . . . . H
# . H . . .
# . . . H .
#
#3.
# . . H . .
# H . . . .
# . . . H .
# . H . . .
# . . . . H
#
#4.
# . . . H .
# H . . . .
# . . H . .
# . . . . H
# . H . . .
#
#5.
# . H . . .
# . . . H .
# H . . . .
# . . H . .
# . . . . H
#
#6.
# . . . . H
# . . H . .
# H . . . .
# . . . H .
# . H . . .
#
#7.
# . H . . .
# . . . . H
# . . H . .
# H . . . .
# . . . H .
#
#8.
# . . . . H
# . H . . .
# . . . H .
# H . . . .
# . . H . .
#
#9.
# . . . H .
# . H . . .
# . . . . H
# . . H . .
# H . . . .
#
#10.
# . . H . .
# . . . . H
# . H . . .
# . . . H .
# H . . . .


