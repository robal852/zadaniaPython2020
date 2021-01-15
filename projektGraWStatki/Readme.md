# Projekt Język Python: "Gra w Statki"

## Zasady:

Gra dla dwóch graczy, gdzie każdy z nich może grać jako człowiek lub komputer.<br />
Każdy ma w swojej flocie:
 - czteromasztowiec (1 szt),<br />
 - trzymasztowiec  (2 szt),<br />
 - dwumasztowiec (3 szt), <br />
 - jednomasztowiec (4 szt).<br />

Na początku należy rozstawić swoje statki na planszy o wymiarach 10x10.<br />
Statki nie mogą się stykać (nawet kątami).<br />
Komputer swoje statki rozstawia automatycznie metodą brute force.<br />
Człowiek może użyćlosowego rozstawienia lub zrobić to samodzielnie.<br />
Zaczyna gracz 1 i gracze na zmianę oddają strzały.<br />
Za każde trafienie jest dodatkowy strzał.<br />
Aby oddać strzał, należy wpisać współrzędne składające się z litery i cyfry.<br />
Można używać małych lub dużych liter. Zakres wsółrzędnych to A-J i 0-9. 

## Legenda:
~~~~python
~ - woda
S - statek
o - pudło
+ - trafiony
X - trafiony-zatopiony
~~~~

## Jak gra komputer?

Komputer strzela losowo do momentu, gdy trafi w statek przeciwnika. <br />
Gdy już wie, że trafił, to celuje obok tego pola. <br />
Gdy trafi drugi raz, a statek będzie wciąż nie zatopiony,<br />
to komputer strzela na tej współrzędnej, wzdłuż której są już trafione pola. <br />
Gdy już zatopi statek, znów zaczyna strzelać losowo, <br />
ale nigdy nie strzela obok zatopionego statku.




## Opis Klas:

~~~python
class Game:
    """ Główna klasa reprezentująca gre w statki """
~~~
Główna klasa, w jej konstruktorze wybieramy zawodników i rozstawiamy statki.<br />
Posiada również metodę startGame(), która uruchamia rozgrywkę. <br />
Jest tu też odpowiednia metoda do sprawdzenia gra powinna się już skończyć. <br />
Tutaj też wywołuje rysowanie planszy oraz komunikaty po strzale. 









~~~python
class Board:
    """ Klasa reprezentująca planszę do gry (10x10) """
~~~
Klasa, gdzie przechowywana jest tablica o rozmiarze 10x10. <br />
Przechowywane w niej wartości mają swoje znaczenie:
```python
        0 oznacza wode                       ~
        1 oznacza statek                     S
        2 oznacza pudlo                      o
        3 oznacza trafiony                   +
        4 oznacza trafiony zatopiony         X
```
Posiada metody które umożliwiają: <br />
- rysowanie planszy z możliwością wybrania czy chcemy widzieć statki<br />
- zatopienie statku w odpowiednim momencie. <br />
- wybieranie współrzędnych<br />
- sprawdzanie sąsiadów danej wspołrzędnej (np. przy ustawianiu statków).

~~~python
class Player:
    """ Klasa reprezentująca gracza (czlowiek lub komputer)"""
~~~
Głównym zadaniem klasy Player jest umożliwienie oddawania strzałów. <br />
Przechowuje informację na temat gracza:<br />
- czy to człowiek czy komputer,
- ile pozostało mu niezatopionych statków.

## Jak zacząć?
Aby zacząć grę uruchamiamy skrypt main.py

## Autor
Albert Surmacz

## Wersja Python
Python 3.8.6

