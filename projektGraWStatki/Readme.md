Projekt Język Python: "Gra w Statki"

Zasady:

Gra dla dwóch graczy (możliwość wyboru człowiek/komputer). Każdy ma w swojej flocie czteromasztowiec, dwa trzymasztowce, trzy dwumasztowce oraz cztery jednomasztowce.
Na początku należy rozstawić swoje statki na planszy 10x10. Statki nie mogą się stykać (nawet kątami). Komputer swoje statki rozstawia automatycznie metodą brute force.
Człowiek ma możliwość ustawienia swoich statków samodzielnie lub rozstawić automatycznie.
Zaczyna gracz 1 i gracze na zmianę oddają strzały, za każde trafienie jest dodatkowy strzał. Aby oddać strzał, należy wpisać współrzędne składające się z litery i cyfry. Przykład: "a6".
Zakres A-J i 0-9. Można używać małych lub dużych liter.

Jak gra komputer?

Komputer strzela losowo do momentu, gdy trafi w statek przeciwnika. Gdy już wie, że trafił, to celuje obok tego pola. Gdy trafi drugi raz, a statek będzie wciąż nie zatopiony,
to komputer strzela na tej współrzędnej, wzdłuż której są już trafione pola. Gdy już zatopi statek, znów zaczyna strzelać losowo, ale nigdy nie strzela obok zatopionego statku.

~~~~
Legenda:
~ - woda
S - statek
o - pudło
+ - trafiony
X - trafiony-zatopiony
~~~~



Albert Surmacz
10.01.2021


Python 3.8.6

