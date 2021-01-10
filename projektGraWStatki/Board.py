import random


class Board:
    """ Klasa reprezentująca planszę do gry (10x10) """

    def __init__(self):
        ''' Plansza zawiera statki i historie gdzie zostal ooddany strzal '''
        self.gameBoard = []
        x = 0
        for i in range(10):
            y = []
            for j in range(10):
                y.append(0)
                x += 1
            self.gameBoard.append(y)

    def setBoardManually(self, player):
        ''' Ustawianie statków na planszy '''
        self.addShipManually(size=4)
        self.addShipManually(size=3)
        self.addShipManually(size=3)
        self.addShipManually(size=2)
        self.addShipManually(size=2)
        self.addShipManually(size=2)
        self.addShipManually(size=1)
        self.addShipManually(size=1)
        self.addShipManually(size=1)
        self.addShipManually(size=1)
        player.aliveShips += 10

    def setBoardAuto(self, player):
        ''' Ustawianie automatyczne dla komputera lub dla leniwego '''
        self.addShip(size=4)
        self.addShip(size=3)
        self.addShip(size=3)
        self.addShip(size=2)
        self.addShip(size=2)
        self.addShip(size=2)
        self.addShip(size=1)
        self.addShip(size=1)
        self.addShip(size=1)
        self.addShip(size=1)
        player.aliveShips += 10

    def addShip(self, size):
        ''' Metodą brute force losuje gdzie upchnąć statek,
         size - dlugosc statku '''
        while True:
            correct = True
            direction = random.randint(0, 1)  # 1 poziom, 0 pion
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if direction == 0:
                for i in range(0, size):
                    if (self.isFieldAvailable(x + i, y, field=1) == False):
                        correct = False
            elif direction == 1:
                for i in range(0, size):
                    if (self.isFieldAvailable(x, y + i, field=1) == False):
                        correct = False
            if (correct):  # przeszlo wiec dodaje statek
                if direction == 0:
                    for i in range(0, size):
                        self.gameBoard[x + i][y] = 1
                elif direction == 1:
                    for i in range(0, size):
                        self.gameBoard[x][y + i] = 1
                break  # koniec nieskonczonej petli

    def addShipManually(self, size):
        '''ręczne ustawianie statków na planszy,
         size - dlugosc statku '''
        dir = {
            0: "poziom",
            1: "pion",
            2: "jednomasztowiec"
        }
        dir2 = {
            1: "jednomasztowiec",
            2: "dwumasztowiec",
            3: "trzymasztowiec",
            4: "czteromasztowiec",
        }
        direction = -1
        if size == 1:
            direction = 2
        self.printBoard()
        print("Ustawiasz", dir2.get(size))
        if size > 1:
            print("Najpierw zdecyduj czy statek ma byc pionowo czy poziomo.")
            while direction != 1 and direction != 0:
                try:
                    direction = int(input("Pionowo wpisz 1, poziomo wpisz 0: "))
                except ValueError:
                    print("Wpisz poprawnie! 0 lub 1")
        print("wybrano: ", dir.get(direction))

        isShipAdded = False
        while not isShipAdded:
            print("Teraz podaj pierwsza wspolrzedna swojego statku.(LiteraCyfra np. A0) "
                  "\n Pamietaj ze statki nie moga sie stykac!")
            XY = ""
            X, Y = -1, -1
            while X == -1 or Y == -1:
                XY = self.getCoordinates()
                X = XY[0]
                Y = XY[1]
            correct = True
            if direction == 1:
                for i in range(0, size):
                    if (self.isFieldAvailable(X + i, Y, field=1) == False):
                        correct = False
            elif direction == 0:
                for i in range(0, size):
                    if (self.isFieldAvailable(X, Y + i, field=1) == False):
                        correct = False
            elif direction == 2:  # jednomasztowiec
                if (self.isFieldAvailable(X, Y, field=1) == False):
                    correct = False
            if (correct):  # przeszlo wiec dodaje statek
                if direction == 1:
                    for i in range(0, size):
                        self.gameBoard[X + i][Y] = 1
                elif direction == 0:
                    for i in range(0, size):
                        self.gameBoard[X][Y + i] = 1
                elif direction == 2:  # jednomasztowiec
                    self.gameBoard[X][Y] = 1
                isShipAdded = True

    def getCoordinates(self):
        correct = False
        XY = ""
        X, Y = -1, -1
        while not correct:
            X, Y = -1, -1
            XY = input("Podaj wspolrzedna ")
            if len(XY) >= 2:
                if ord(XY[0]) > 64 and ord(XY[0]) < 75:
                    X = ord(XY[0]) - 65
                if ord(XY[0]) > 96 and ord(XY[0]) < 107:
                    X = ord(XY[0]) - 97
                if ord(XY[1]) > 47 and ord(XY[1]) < 58:
                    Y = ord(XY[1]) - 48
            if X != -1 and Y != -1:
                correct = True
        return [X, Y]

    def isFieldAvailable(self, x, y, field):
        ''' Sprawdzam pole z planszy i jego otoczenie czy nadaje sie na statek
        field to pole jakiego nie moze miec w poblizu
        '''
        if x > 9:
            return False
        elif y > 9:
            return False
        elif x == 0:
            if y == 0:
                if self.gameBoard[x][y] == field or self.gameBoard[x + 1][y] == field or self.gameBoard[x][y + 1] or \
                        self.gameBoard[x + 1][y + 1] == field:
                    return False  # statek nie moze sie stykac ze statkiem
                else:
                    return True
            elif y == 9:
                if self.gameBoard[x][y] == field or self.gameBoard[x + 1][y] == field or self.gameBoard[x][
                    y - 1] == field or \
                        self.gameBoard[x + 1][y - 1] == field:
                    return False
                else:
                    return True
            else:
                if self.gameBoard[x][y] == field or self.gameBoard[x + 1][y] == field or self.gameBoard[x][
                    y - 1] == field or \
                        self.gameBoard[x][y + 1] == field or self.gameBoard[x + 1][y - 1] == field or \
                        self.gameBoard[x + 1][
                            y + 1] == field:
                    return False
                else:
                    return True
        elif x == 9:
            if y == 0:
                if self.gameBoard[x][y] == field or self.gameBoard[x - 1][y] == field or self.gameBoard[x][
                    y + 1] == field or \
                        self.gameBoard[x - 1][y + 1] == field:
                    return False
                else:
                    return True
            elif y == 9:
                if self.gameBoard[x][y] == field or self.gameBoard[x - 1][y] == field or self.gameBoard[x][
                    y - 1] == field or \
                        self.gameBoard[x - 1][y - 1] == field:
                    return False
                else:
                    return True
            else:
                if self.gameBoard[x][y] == field or self.gameBoard[x - 1][y] == field or self.gameBoard[x][
                    y - 1] == field or \
                        self.gameBoard[x][y + 1] == field or self.gameBoard[x - 1][y + 1] == field or \
                        self.gameBoard[x - 1][
                            y - 1] == field:
                    return False
                else:
                    return True
        elif y == 0:
            if self.gameBoard[x][y] == field or self.gameBoard[x - 1][y] == field or self.gameBoard[x + 1][
                y] == field or \
                    self.gameBoard[x][y + 1] == field or self.gameBoard[x - 1][y + 1] == field or self.gameBoard[x + 1][
                y + 1] == field:
                return False
            else:
                return True
        elif y == 9:
            if self.gameBoard[x][y] == field or self.gameBoard[x - 1][y] == field or self.gameBoard[x + 1][
                y] == field or \
                    self.gameBoard[x - 1][y - 1] == field or self.gameBoard[x][y] == field or self.gameBoard[x][
                y - 1] == field or \
                    self.gameBoard[x + 1][y - 1] == field:
                return False
            else:
                return True
        else:  # 9 pol srodek i 8 dookola
            if self.gameBoard[x][y] == field or self.gameBoard[x - 1][y] == field or self.gameBoard[x + 1][
                y] == field or \
                    self.gameBoard[x][y - 1] == field or self.gameBoard[x][y + 1] == field or self.gameBoard[x - 1][
                y - 1] == field or self.gameBoard[x + 1][y + 1] == field or self.gameBoard[x - 1][y + 1] == field or \
                    self.gameBoard[x + 1][y - 1] == field:
                return False
            else:
                return True

    def printBoard(self, visibleShips=True):
        ''' Metoda do wyswietlenia stanu gry '''
        print("  ", end="")
        for i in range(10):
            print("", i, end="")
        print("")
        vertical = "ABCDEFGHIJ"
        for i in range(10):
            print(vertical[i], end=" ")
            for j in range(10):
                self.printSymbol(self.gameBoard[i][j], visibleShips)
            print("")  # nowa linia

    def printSymbol(self, number, visibleShips):
        '''
        0 oznacza wode                       ~
        1 oznacza statek                     S
        2 oznacza pudlo                      o
        3 oznacza trafiony                   +
        4 oznacza trafiony zatopiony         X
        '''
        switcher = {
            0: " ~",
            1: " S",
            2: " o",
            3: " +",
            4: " X"
        }
        switcher2 = {
            0: " ~",
            1: " ~",  # ukryte statki
            2: " o",
            3: " +",
            4: " X"
        }
        if (visibleShips):
            symbol = switcher.get(number)
        else:
            symbol = switcher2.get(number)
        print(symbol, end="")

    def checkIfSunk(self, x, y):
        ''' sprawdza czy statek juz zatopiony '''
        self.gameBoard[x][y] = 4  # zeby pominal to pole
        # sprawdzam czy ma kontakt z zywym statkiem
        # narozniki
        if x == 0 and y == 0:
            if self.gameBoard[x + 1][y] == 1 or self.gameBoard[x][y + 1] == 1:
                self.gameBoard[x][y] = 3
                return False
        if x == 9 and y == 0:
            if self.gameBoard[x - 1][y] == 1 or self.gameBoard[x][y + 1] == 1:
                self.gameBoard[x][y] = 3
                return False
        if x == 9 and y == 9:
            if self.gameBoard[x - 1][y] == 1 or self.gameBoard[x][y - 1] == 1:
                self.gameBoard[x][y] = 3
                return False
        if x == 0 and y == 9:
            if self.gameBoard[x + 1][y] == 1 or self.gameBoard[x][y - 1] == 1:
                self.gameBoard[x][y] = 3
                return False
        # krawedzie bez naroznikow
        if x > 0 and x < 9 and y == 0:
            if self.gameBoard[x + 1][y] == 1 or self.gameBoard[x - 1][y] == 1 or self.gameBoard[x][y + 1] == 1:
                self.gameBoard[x][y] = 3
                return False
        if x > 0 and x < 9 and y == 9:
            if self.gameBoard[x + 1][y] == 1 or self.gameBoard[x - 1][y] == 1 or self.gameBoard[x][y - 1] == 1:
                self.gameBoard[x][y] = 3
                return False
        if y > 0 and y < 9 and x == 0:
            if self.gameBoard[x + 1][y] == 1 or self.gameBoard[x][y - 1] == 1 or self.gameBoard[x][y + 1] == 1:
                self.gameBoard[x][y] = 3
                return False

        if y > 0 and y < 9 and x == 9:
            if self.gameBoard[x - 1][y] == 1 or self.gameBoard[x][y - 1] == 1 or self.gameBoard[x][y + 1] == 1:
                self.gameBoard[x][y] = 3
                return False
        # srodek
        if x > 0 and x < 9 and y > 0 and y < 9:
            if self.gameBoard[x + 1][y] == 1 or self.gameBoard[x - 1][y] == 1 or self.gameBoard[x][y + 1] == 1 or \
                    self.gameBoard[x][y - 1] == 1:
                self.gameBoard[x][y] = 3
                return False
        # sprawddzic czy ma kontakt z trafionym zeby znalezc gdy juz zatopilem

        # sprawdzam czy ma kontakt z trafionym, jak ma kontakt to od nowa dla tego pola sprawdzam
        # narozniki
        if x == 0 and y == 0:
            if self.gameBoard[x + 1][y] == 3:
                if not self.checkIfSunk(x + 1, y):
                    self.gameBoard[x][y] = 3
                    return False
            if self.gameBoard[x][y + 1] == 3:
                if not self.checkIfSunk(x, y + 1):
                    self.gameBoard[x][y] = 3
                    return False

        if x == 9 and y == 0:
            if self.gameBoard[x - 1][y] == 3:
                if not self.checkIfSunk(x - 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x][y + 1] == 3:
                if not self.checkIfSunk(x, y + 1):
                    self.gameBoard[x][y] = 3
                    return False

        if x == 9 and y == 9:
            if self.gameBoard[x - 1][y] == 3:
                if not self.checkIfSunk(x - 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x][y - 1] == 3:
                if not self.checkIfSunk(x, y - 1):
                    self.gameBoard[x][y] = 3
                    return False

        if x == 0 and y == 9:
            if self.gameBoard[x + 1][y] == 3:
                if not self.checkIfSunk(x + 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x][y - 1] == 3:
                if not self.checkIfSunk(x, y - 1):
                    self.gameBoard[x][y] = 3
                    return False
        # krawedzie bez naroznikow
        if x > 0 and x < 9 and y == 0:
            if self.gameBoard[x + 1][y] == 3:
                if not self.checkIfSunk(x + 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x - 1][y] == 3:
                if not self.checkIfSunk(x - 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x][y + 1] == 3:
                if not self.checkIfSunk(x, y + 1):
                    self.gameBoard[x][y] = 3
                    return False

        if x > 0 and x < 9 and y == 9:
            if self.gameBoard[x + 1][y] == 3:
                if not self.checkIfSunk(x + 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x - 1][y] == 3:
                if not self.checkIfSunk(x - 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x][y - 1] == 3:
                if not self.checkIfSunk(x, y - 1):
                    self.gameBoard[x][y] = 3
                    return False

        if y > 0 and y < 9 and x == 0:
            if self.gameBoard[x + 1][y] == 3:
                if not self.checkIfSunk(x + 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x][y - 1] == 3:
                if not self.checkIfSunk(x, y - 1):
                    self.gameBoard[x][y] = 3
                    return False

        if y > 0 and y < 9 and x == 9:
            if self.gameBoard[x - 1][y] == 3:
                if not self.checkIfSunk(x - 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x][y - 1] == 3:
                if not self.checkIfSunk(x, y - 1):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x][y + 1] == 3:
                if not self.checkIfSunk(x, y + 1):
                    self.gameBoard[x][y] = 3
                    return False
        # srodek
        if x > 0 and x < 9 and y > 0 and y < 9:
            if self.gameBoard[x + 1][y] == 3:
                if not self.checkIfSunk(x + 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x - 1][y] == 3:
                if not self.checkIfSunk(x - 1, y):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x][y + 1] == 3:
                if not self.checkIfSunk(x, y + 1):
                    self.gameBoard[x][y] = 3
                    return False

            if self.gameBoard[x][y - 1] == 3:
                if not self.checkIfSunk(x, y - 1):
                    self.gameBoard[x][y] = 3
                    return False
        # jak tu doszedlem to zatopiony!!
        return True
