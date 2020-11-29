# Program do wyznaczania liczby π

import math
from random import random


def wyznacz_PI(
        liczba_losowan):  # bede losowal punkt i sprawdzial czy wylosowany punkt ma odleglosc mniejsza lub rowna 1 od punktu (0,0)
    trafiony = 0  # ile razy trafilem w cwiartke kola
    for i in range(liczba_losowan):
        x = random()
        y = random()
        odleglosc = math.sqrt((x ** 2 + y ** 2))  # obliczam odleglosc - pierwiastek z sumy kwadratow wspolrzednych
        if odleglosc <= 1:
            trafiony += 1

        # PI / 4 = trafiony / ile razy strzelalem
    obliczona_liczba_PI = (trafiony / liczba_losowan) * 4;
    print("Liczba PI obliczona dla ", liczba_losowan, " losowan wynosi:", obliczona_liczba_PI)


if __name__ == "__main__":
    liczba_losowan = 10
    while (liczba_losowan < 10000000):
        wyznacz_PI(liczba_losowan)
        liczba_losowan = liczba_losowan * 10
