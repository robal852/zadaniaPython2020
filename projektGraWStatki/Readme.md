# Projekt Język Python: "Gra w Statki"

## Zasady:

Gra dla dwóch graczy (możliwość wyboru człowiek/komputer). Każdy ma w swojej flocie czteromasztowiec, dwa trzymasztowce, trzy dwumasztowce oraz cztery jednomasztowce.
Na początku należy rozstawić swoje statki na planszy 10x10. Statki nie mogą się stykać (nawet kątami). Komputer swoje statki rozstawia automatycznie metodą brute force.
Człowiek ma możliwość ustawienia swoich statków samodzielnie lub rozstawić automatycznie.
Zaczyna gracz 1 i gracze na zmianę oddają strzały, za każde trafienie jest dodatkowy strzał. Aby oddać strzał, należy wpisać współrzędne składające się z litery i cyfry. Przykład: "a6".
Zakres A-J i 0-9. Można używać małych lub dużych liter.

## Legenda:
~~~~
~ - woda
S - statek
o - pudło
+ - trafiony
X - trafiony-zatopiony
~~~~

## Jak gra komputer?

Komputer strzela losowo do momentu, gdy trafi w statek przeciwnika. Gdy już wie, że trafił, to celuje obok tego pola. Gdy trafi drugi raz, a statek będzie wciąż nie zatopiony,
to komputer strzela na tej współrzędnej, wzdłuż której są już trafione pola. Gdy już zatopi statek, znów zaczyna strzelać losowo, ale nigdy nie strzela obok zatopionego statku.




## Opis Klas:

~~~
class Game:
    """ Główna klasa reprezentująca gre w statki """
~~~
Główna klasa to Game, w jej konstruktorze uruchamiana jest metoda setUp,
 w której wybieramy zawodników i rozstawiamy statki.
 Klasa ta posiada również metodę startGame(), która uruchamia rozgrywkę.
 Tutaj również sprawdzane jest czy ktoś przegrałaby w odpowiednim momencie zakończyć program.
 Ostatnie zadania tej klasy to rysowanie planszy oraz komunikaty po strzale z informacją czy trafiliśmy czy też nie. 









~~~
class Board:
    """ Klasa reprezentująca planszę do gry (10x10) """
~~~
Kolejna to Board, gdzie przechowywana jest tablica wartosci int o rozmiarze 10x10.
Przechowywane wartości mająswoje znaczenie:
```
        0 oznacza wode                       ~
        1 oznacza statek                     S
        2 oznacza pudlo                      o
        3 oznacza trafiony                   +
        4 oznacza trafiony zatopiony         X
```
Znajdziemy tu metody do rysowania planszy z możliwościąwybrania czy chcemy widzieć statki.
Odpowiedzialna jest rónież za zatopienie statku w odpowiednim momencie.
Pozwala na wybieranie współrzędnych oraz na sprawdzanie sąsiadów danej wspołrzędnej (używane przy strzale i ustawianiu statków).

~~~
class Player:
    """ Klasa reprezentująca gracza (czlowiek lub komputer)"""
~~~
Głównym zadaniem klasy Player jest umożliwienie oddawania strzałów.
Przechowuje również informację czy to człowiek czy komputer, oraz ile pozostało mu niezatopionych statków.

## Jak zacząć?
Aby zacząć grę uruchamiamy skrypt main.py

## Autor
Albert Surmacz

## Wersja Python
Python 3.8.6

