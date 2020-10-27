# Zestaw zadan 3.
# Albert Surmacz
# 24.10.2020

# ZADANIE 3.1
# Czy podany kod jest poprawny skladniowo w Pythonie? Jesli nie, to dlaczego?
# x = 2;
# y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y
# Nie potrzeba pisac srednikow ani nawiasi ale kod sie wykona poprawnie.

# for i in "qwerty": if ord(i) < 100: print (i) # Blad skladni, musi byc nowa linia
# Poprawione:
# for i in "qwerty":
#     if ord(i) < 100: print(i)

# for i in "axby": print(ord(i) if ord(i) < 100 else i)
# Wykona sie poprawnie, ale czytelniej gdy zapiszemy z instrukcja print w nowej linii z wcieciem.


# zadanie 3.2
# Co jest zlego w kodzie:
# L = [3, 5, 4] ; L = L.sort() #Blednie: do L zostanie przypisany void, sort sortuje liste ale niepotrzebnie przypisujemy wynik, bo to nie zwraca posortowanej listy!

# x, y = 1, 2, 3 # Blednie: przypisanie krotki (pozycyjne) brakuje trzeciej pozycji np. x, y, z = 1, 2, 3

# X = 1, 2, 3 ; X[1] = 4 #Blednie: krotka nie ma dosteou przez operator zakresu

# X = [1, 2, 3] ; X[3] = 4 #Blednie: x[3] odnosi się poza zakres, bo indeksujemy od zera, więc mamy dostępne 0, 1, 2

# X = "abc" ; X.append("d") #Blednie: 'str' object has no attribute 'append'

# L = list(map(pow, range(8))) #Blednie: funkcja pow otrzymuje tylko jeden argument, a potrzebuje dwa

# zadanie 3.3
print("Zadanie 3.3")
# Wypisać w petli liczby od 0 do 30 z wyjatkiem liczb podzielnych przez 3.
for i in range(31):
    if i % 3:
        print(i, end=', ')

# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący parę x i trzecią potęgę x.
# Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
# Jezeli uzytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.
# Zadanie 3.4
print("\n\nZadanie 3.4")

while 1:
    x = input("Podaj liczbe lub wpisz stop: ")
    if (x == "stop"):
        break
    try:
        x = float(x)
    except ValueError:
        print("Bledne dane")
        continue
    print("Podana liczba to: " + str(x) + " ,a jej trzecia potega to: " + str(pow(float(x), 3)))

# Napisać program rysujący "miarkę" o zadanej długości.
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
# (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
# Należy zbudować pełny string, a potem go wypisać.
# |....|....|....|....|....|....|....|....|....|....|....|....|
# 0    1    2    3    4    5    6    7    8    9   10   11   12
# Zadanie 3.5
print("\n\nZadanie 3.5")


def printTape(x):
    length = x
    tape = ""
    for i in range(int(length)):
        tape += "|"
        numOfDots = 3 + len(str(length))
        for j in range(numOfDots):
            tape += "."
    tape += "|\n"
    for i in range(int(length)):
        tape += str(i)
        numOfSpaces = (4 + (len(str(length)) - len(str(i))))
        for j in range(numOfSpaces):
            tape += " "
    lenOfLastDigit = len(str(length))
    if (lenOfLastDigit > 1):
        tape = tape[:-lenOfLastDigit + 1]
    tape += str((int(length)))
    print(tape)


# length = ""
# while not length.isdigit():
#     length = input("Podaj liczbe calkowita: ")
# printTape(length)
printTape(7)
printTape(13)
printTape(105)

# Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+

# Zadanie 3.6
print("\n\nZadanie 3.6")


def printMatrix(x, y):
    if (x < 1 or y < 1):
        return
    rysunek = ""
    for i in range(x):
        for j in range(y):
            rysunek += "+---"
        rysunek += "+\n"
        for j in range(y):
            rysunek += "|   "
        rysunek += "|\n"
    for j in range(y):
        rysunek += "+---"
    rysunek += "+\n"
    print(rysunek)


printMatrix(2, 4)
printMatrix(1, 0)
printMatrix(5, 5)

# Dla dwóch sekwencji znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
# Zadanie 3.8
print("\n\nZadanie 3.8")
from collections import Counter

print("\n\nZadanie 3.8")
seq1 = "abcdefghijk12345555"
seq2 = "abcd              56789999"
print("sekwencja 1 to: " + seq1)
print("sekwencja 2 to: " + seq2)

dict1 = Counter(seq1)
dict2 = Counter(seq2)

print("lista elementow wystepujacych jednoczesnie w obu sekwencjach (bez powtorzen) to: ")
commonDict = dict1 & dict2
commonChars = set(commonDict.elements())
print(''.join(commonChars))

print("lista wszystkich elementow z obu sekwencji (bez powtorzen) to: ")
sumDict = dict1 | dict2
allChars = set(sumDict.elements())
print(''.join(allChars))

# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
# Znaleźć listę zawierającą sumy liczb z tych sekwencji.
# Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].
# Zadanie 3.9
print("\n\nZadanie 3.9")
lista = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
listaWynik = []
for i in lista:
    listaWynik.append(sum(i))
print(listaWynik)

# Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie
# (podać kilka sposobów tworzenia takiego słownika).
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
# Zadanie 3.10
print("\n\nZadanie 3.10")

dict1 = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    " ": 0
}
dict2 = dict(I=1,
             V=5,
             X=10,
             L=50,
             C=100,
             D=500,
             M=1000)

data = ['I', 'V', 'X', 'L', 'C', 'D', 'M'];
dict3 = dict.fromkeys(data, 1)
dict3['V'] = 5
dict3['X'] = 10
dict3['L'] = 50
dict3['C'] = 100
dict3['D'] = 500
dict3['M'] = 1000

print(dict1)
print(dict2)
print(dict3)
print()
import re


def isCorrectRomanNumber(roman):
    return bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman))


def roman2int(roman):
    if not isCorrectRomanNumber(roman):
        print("Liczba jest niepoprawna!")
        return -1
    caffeArabica = 0
    roman += " "
    skipOneLoop = False
    for i in range(len(roman) - 1):
        if skipOneLoop:
            skipOneLoop = False
            continue
        if (dict1.get(roman[i + 1]) <= dict1.get(roman[i])):
            caffeArabica += dict1.get(roman[i])
        else:
            caffeArabica += dict1.get(roman[i + 1])
            caffeArabica -= dict1.get(roman[i])
            skipOneLoop = True
    return caffeArabica


print(roman2int("CMXCIX"))
print(roman2int("VV"))
print(roman2int("VII"))
