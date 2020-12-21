# Problem drogi skoczka na kwadratowej szachownicy o boku N.
# Współrzędne planszy x i y mają zakres od 0 do N-1.

def rysuj():
    for i in range(N):
        print(" ".join("{0:2d}".format(plansza[i, j]) for j in range(N)))


def dopuszczalny(x, y):
    return 0 <= x < N and 0 <= y < N and plansza[x, y] == 0


def zapisz(krok, x, y):
    plansza[x, y] = krok  # zapis ruchu


def wymaz(x, y):
    plansza[x, y] = 0


def probuj(krok, x, y):
    # krok - nr kolejnego kroku do zrobienia
    # x, y - pozycja startowa skoczka
    # Funkcja zwraca bool True/False (czy udany ruch).
    udany = False
    kandydat = 0  # numery od 0 do RUCHY_SKOCZKA-1
    while (not udany) and (kandydat < RUCHY_SKOCZKA):
        u = x + delta_x[kandydat]  # wybieramy kandydata
        v = y + delta_y[kandydat]
        if dopuszczalny(u, v):
            zapisz(krok, u, v)
            if krok < N * N:  # warunek końca rekurencji
                udany = probuj(krok + 1, u, v)
                if not udany:
                    wymaz(u, v)
            else:
                udany = True
        kandydat += 1
    return udany


N = 6  # bok szachownicy
RUCHY_SKOCZKA = 8

# Inicjalizacja pustej planszy.
plansza = {}
for i in range(N):
    for j in range(N):
        plansza[i, j] = 0

# . 2 . 1 .   kolejne możliwe ruchy skoczka
# 3 . . . 0
# . . x . .
# 4 . . . 7
# . 5 . 6 .

delta_x = [2, 1, -1, -2, -2, -1, 1, 2]  # różnica współrzędnej x
delta_y = [1, 2, 2, 1, -1, -2, -2, -1]  # różnica współrzędnej y
(x0, y0) = (0, 2)  # pole startowe skoczka

zapisz(1, x0, y0)

if probuj(2, x0, y0):
    print("Mamy rozwiązanie")
    rysuj()
else:
    print("Nie istnieje rozwiązanie")

# Rozwiązania dla szachownicy 6x6:
#
#  1 16  7 26 11 14   14  1 20  7 12  9    7 26  1 22  5 24
# 34 25 12 15  6 27   19 34 13 10 21  6   36 15  6 25 34 21
# 17  2 33  8 13 10   28 15  2 33  8 11   27  8 35  2 23  4
# 32 35 24 21 28  5   35 18 29 24  5 22   16 11 14 31 20 33
# 23 18  3 30  9 20   30 27 16  3 32 25   13 28  9 18  3 30
# 36 31 22 19  4 29   17 36 31 26 23  4   10 17 12 29 32 19
#
#                     19 28 35 26 21  6   36 17  6 29  8 11
#                     36  1 20  7 34 25   19 30  1 10  5 28
#                     29 18 27 24  5 22   16 35 18  7 12  9
#                     12 15  2 31  8 33   23 20 31  2 27  4
#                     17 30 13 10 23  4   34 15 22 25 32 13
#                     14 11 16  3 32  9   21 24 33 14  3 26
#
#                                         31 34 15  6 25 36
#                                         16 23 32 35 14  5
#                                         33 30  1 24  7 26
#                                         20 17 22 11  4 13
#                                         29 10 19  2 27  8
#                                         18 21 28  9 12  3
#
# pozostałe rozwiązania symetrycznie do tych przedstawionych powyzej