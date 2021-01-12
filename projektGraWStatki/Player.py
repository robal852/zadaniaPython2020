import random
import time


class Player:
    """ Klasa reprezentująca gracza (czlowiek lub komputer)"""

    def __init__(self, isHuman):
        """ isHuman true to czlowiek, false to komputer """
        self.isHuman = isHuman
        self.aliveShips = 0

    def __str__(self):
        if self.isHuman:
            return "Czlowiek"
        else:
            return "Komputer"

    def isLoser(self):
        ''' Sprzadzam czy przegral'''
        if self.aliveShips > 0:
            return False
        else:
            return True

    def move(self, opponentBoard, opponent):
        ''' Ruch czlowieka lub komputera '''

        if not self.isHuman:
            print("Ruch komputera")
            # Tu Mmge opoznic ruchy komputera zeby widziec co sie dzieje np przy pojedynku komputer vs komputer
            time.sleep(1)

        success = False
        while not success:
            if self.isHuman:
                print("Twoj ruch!")
                XY = opponentBoard.getCoordinates()
                X = XY[0]
                Y = XY[1]

            # czesc komputera
            else:
                alreadyHitted = []  # tutaj sobie zapisze gdzie juz trafil, a jeszcze nie zatopil
                for i in range(0, 10):
                    for j in range(0, 10):
                        if opponentBoard.gameBoard[i][j] == 3:
                            alreadyHitted.append([i, j])
                # tylko jedno trafione pole wiec bede obok strzelal
                if len(alreadyHitted) == 1:
                    X = alreadyHitted[0][0]
                    Y = alreadyHitted[0][1]
                    while opponentBoard.gameBoard[X][Y] != 0 and opponentBoard.gameBoard[X][
                        Y] != 1:  # nie chce strzelac tam gdzie juz strzelalem - zostaje woda albo statek
                        rand = random.randint(0, 3)  # jedno z 4 obok trafionego: gora, dol, prawo, lewo
                        X = alreadyHitted[0][0]
                        Y = alreadyHitted[0][1]
                        if rand == 0:
                            if X < 9:
                                X += 1
                            else:
                                X -= 1
                        elif rand == 1:
                            if Y < 9:
                                Y += 1
                            else:
                                Y -= 1
                        elif rand == 2:
                            if X > 0:
                                X -= 1
                            else:
                                X += 1
                        elif rand == 3:
                            if Y > 0:
                                Y -= 1
                            else:
                                Y += 1
                # gdy conajmniej dwa trafione pola to w tej samej linii strzeli
                elif len(alreadyHitted) > 1:  # wykryc kierunek
                    X = alreadyHitted[0][0]
                    Y = alreadyHitted[0][1]
                    while opponentBoard.gameBoard[X][Y] != 0 and opponentBoard.gameBoard[X][Y] != 1:
                        rand = random.randint(0, 1)
                        if alreadyHitted[0][0] == alreadyHitted[1][0]:  # X taki sam wiec zmieniam tylko Y
                            X = alreadyHitted[0][0]
                            maxY = alreadyHitted[0][1]
                            minY = alreadyHitted[0][1]
                            for i in alreadyHitted:
                                if i[1] > maxY:
                                    maxY = i[1]
                                if i[1] < minY:
                                    minY = i[1]
                            if minY == 0:
                                Y = maxY + 1
                            elif maxY == 9:
                                Y = minY - 1
                            elif rand == 0:
                                Y = maxY + 1
                            elif rand == 1:
                                Y = minY - 1
                        else:  # Y taki sam wiec zmieniam tylko X
                            rand = random.randint(0, 1)
                            X = alreadyHitted[0][0]
                            Y = alreadyHitted[0][1]
                            while opponentBoard.gameBoard[X][Y] == 3:
                                Y = alreadyHitted[0][1]
                                maxX = alreadyHitted[0][0]
                                minX = alreadyHitted[0][0]
                                for i in alreadyHitted:
                                    if i[0] > maxX:
                                        maxX = i[0]
                                    if i[0] < minX:
                                        minX = i[0]
                                if minX == 0:
                                    X = maxX + 1
                                elif maxX == 9:
                                    X = minX - 1
                                elif rand == 0:
                                    X = maxX + 1
                                elif rand == 1:
                                    X = minX - 1
                else:  # nie ma zadnego trafionego
                    X = random.randint(0, 9)
                    Y = random.randint(0, 9)

            # komputer nie strzela obok zatopionego!
            if not self.isHuman and not opponentBoard.isFieldAvailable(X, Y, field=4):
                success = False
            else:
                # czesc wspolna czlowiek-komputer sprawdzam czy poprawny strzal i zaznaczam na planszy
                if opponentBoard.gameBoard[X][Y] == 2 or opponentBoard.gameBoard[X][Y] == 3 or \
                        opponentBoard.gameBoard[X][Y] == 4:
                    success = False
                elif opponentBoard.gameBoard[X][Y] == 0 or opponentBoard.gameBoard[X][Y] == 1:  # woda albo statek
                    success = True
                    if opponentBoard.gameBoard[X][Y] == 0:
                        opponentBoard.gameBoard[X][Y] = 2  # pudlo
                        return False
                    elif opponentBoard.gameBoard[X][Y] == 1:
                        opponentBoard.gameBoard[X][Y] = 3  # trafiony
                        if opponentBoard.checkIfSunk(X, Y):  # trafiony-zatopiony
                            opponent.aliveShips -= 1
                        return True
                else:
                    print("Cos poszlo nie tak")
