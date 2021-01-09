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

    def setBoardManually(self):
        ''' Ustawianie statków na planszy '''
        pass

    def setBoardAuto(self):
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

    def addShip(self, size):
        while True:
            correct = True
            direction = random.randint(0, 1)  # 0 poziom, 1 pion
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if direction == 0:
                for i in range(0, size):
                    if (self.isFieldAvailable(x + i, y) == False):
                        correct = False
            elif direction == 1:
                for i in range(0, size):
                    if (self.isFieldAvailable(x, y + i) == False):
                        correct = False
            if(correct):# przeszlo wiec dodaje statek
                if direction == 0:
                    for i in range(0, size):
                        self.gameBoard[x + i][y] = 1
                elif direction == 1:
                    for i in range(0, size):
                        self.gameBoard[x][y + i] = 1
                break  # koniec nieskonczonej petli
        # self.printBoard()
        # print(" ")

    def isFieldAvailable(self, x, y):
        ''' Sprawdzam pole z planszy i jego otoczenie czy nadaje sie na statek '''
        if x > 9:
            return False
        elif y > 9:
            return False
        elif x == 0:
            if y == 0:
                if self.gameBoard[x][y] == 1 or self.gameBoard[x + 1][y] == 1 or self.gameBoard[x][y + 1] or \
                        self.gameBoard[x + 1][y + 1] == 1:
                    return False  # statek nie moze sie stykac ze statkiem
                else:
                    return True
            elif y == 9:
                if self.gameBoard[x][y] == 1 or self.gameBoard[x + 1][y] == 1 or self.gameBoard[x][y - 1] == 1 or \
                        self.gameBoard[x + 1][y - 1] == 1:
                    return False
                else:
                    return True
            else:
                if self.gameBoard[x][y] == 1 or self.gameBoard[x + 1][y] == 1 or self.gameBoard[x][y - 1] == 1 or \
                        self.gameBoard[x][y + 1] == 1 or self.gameBoard[x + 1][y - 1] == 1 or self.gameBoard[x + 1][
                    y + 1] == 1:
                    return False
                else:
                    return True
        elif x == 9:
            if y == 0:
                if self.gameBoard[x][y] == 1 or self.gameBoard[x - 1][y] == 1 or self.gameBoard[x][y + 1] == 1 or \
                        self.gameBoard[x - 1][y + 1] == 1:
                    return False
                else:
                    return True
            elif y == 9:
                if self.gameBoard[x][y] == 1 or self.gameBoard[x - 1][y] == 1 or self.gameBoard[x][y - 1] == 1 or \
                        self.gameBoard[x - 1][y - 1] == 1:
                    return False
                else:
                    return True
            else:
                if self.gameBoard[x][y] == 1 or self.gameBoard[x - 1][y] == 1 or self.gameBoard[x][y - 1] == 1 or \
                        self.gameBoard[x][y + 1] == 1 or self.gameBoard[x - 1][y + 1] == 1 or self.gameBoard[x - 1][
                    y - 1] == 1:
                    return False
                else:
                    return True
        elif y == 0:
            if self.gameBoard[x][y] == 1 or self.gameBoard[x - 1][y] == 1 or self.gameBoard[x + 1][y] == 1 or \
                    self.gameBoard[x][y + 1] == 1 or self.gameBoard[x - 1][y + 1] == 1 or self.gameBoard[x + 1][
                y + 1] == 1:
                return False
            else:
                return True
        elif y == 9:
            if self.gameBoard[x][y] == 1 or self.gameBoard[x - 1][y] == 1 or self.gameBoard[x + 1][y] == 1 or \
                    self.gameBoard[x - 1][y - 1] == 1 or self.gameBoard[x][y] == 1 or self.gameBoard[x][y - 1] == 1 or \
                    self.gameBoard[x + 1][y - 1] == 1:
                return False
            else:
                return True
        else:  # 9 pol srodek i 8 dookola
            if self.gameBoard[x][y] == 1 or self.gameBoard[x - 1][y] == 1 or self.gameBoard[x + 1][y] == 1 or \
                    self.gameBoard[x][y - 1] == 1 or self.gameBoard[x][y + 1] == 1 or self.gameBoard[x - 1][
                y - 1] == 1 or self.gameBoard[x + 1][y + 1] == 1 or self.gameBoard[x - 1][y + 1] == 1 or \
                    self.gameBoard[x + 1][y - 1] == 1:
                return False
            else:
                return True

    def printBoard(self, visibleShips=True):
        ''' Metoda do wyswietlenia stanu gry '''
        for i in range(10):
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
