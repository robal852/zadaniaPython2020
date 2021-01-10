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

        posMessage = {
            0: "TRAFIONY!",
            1: "JESZCZE RAZ I POJDZIE W PIACH!",
            2: "PRZECIWNIK OBERWAL!",
            3: "PODOBALO SIE..? MAM WIECEJ!",
            4: "DORWALISMY GO!",
            5: "WESZLO JAK W MASLO!",
            6: "TO MUSIAL POCZUC!"
        }

        negMessage = {
            0: "PUDLO!",
            1: "TYM GO NIE POKONAMY!",
            2: "BYLO BLISKO",
        }

        success = False
        while not success:
            if self.isHuman:
                print("Twoj ruch!")
                XY = opponentBoard.getCoordinates()
                X = XY[0]
                Y = XY[1]
            else:
                print("Ruch komputera")  # TODO dodac sprawdzenie czy ma w poblizu zatopiony statek
                # time.sleep(2)
                alreadyHitted = []
                for i in range(0, 10):
                    for j in range(0, 10):
                        if opponentBoard.gameBoard[i][j] == 3:
                            alreadyHitted.append([i, j])
                            # TODO INTELIGENTNY RUCH  ZEBY WYKRYL TEZ ZE DWA W JEDNEj LINII TO W TEJ LADUJE
                # print("alreadyHitted", alreadyHitted)
                # print("len", len(alreadyHitted))
                if len(alreadyHitted) == 1:  # tylko jedno trafione pole wiec bede obok strzelal
                    rand = random.randint(0, 3)  # jedno z 4 obok trafionego: gora, dol, prawo, lewo
                    X = alreadyHitted[0][0]
                    Y = alreadyHitted[0][1]
                    # print("HELLLOOO", X, Y)
                    while opponentBoard.gameBoard[X][Y] == 3:
                        X = alreadyHitted[0][0]
                        Y = alreadyHitted[0][1]
                        if rand == 0 and X < 9:  # jak bedzie x=9 to zostanie x i y na tym co bylo czyli pole "trafiony satek"
                            X += 1
                        elif rand == 1 and Y < 9:
                            Y += 1
                        elif rand == 2 and X > 0:
                            X -= 1
                        elif rand == 3 and Y > 0:
                            Y -= 1
                elif len(alreadyHitted) > 1:  # wykryc kierunek
                    rand = random.randint(0, 1)
                    if alreadyHitted[0][0] == alreadyHitted[1][0]:  # X
                        X = alreadyHitted[0][0]
                        maxY = alreadyHitted[0][1]
                        minY = alreadyHitted[0][1]
                        for i in alreadyHitted:
                            if i[0][1] > maxY:
                                maxY = i[0][1]
                            if i[0][1] < minY:
                                minY = i[0][1]
                        if minY == 0:
                            y = maxY + 1
                        elif maxY == 9:
                            y = minY - 1
                        elif rand == 0:
                            Y = maxY + 1
                        elif rand == 1:
                            y = minY - 1

                    else:  # Y
                        Y = alreadyHitted[0][1]
                        maxX = alreadyHitted[0][0]
                        minX = alreadyHitted[0][0]
                        for i in alreadyHitted:
                            if i[0][0] > maxX:
                                maxX = i[0][0]
                            if i[0][0] < minX:
                                minX = i[0][0]
                        if minX == 0:
                            X = maxX + 1
                        elif maxX == 9:
                            X = minX - 1
                        elif rand == 0:
                            X = maxX + 1
                        elif rand == 1:
                            X = minX - 1
                else:
                    X = random.randint(0, 9)
                    Y = random.randint(0, 9)
            if opponentBoard.gameBoard[X][Y] == 0 or opponentBoard.gameBoard[X][Y] == 1:  # woda albo statek
                if opponentBoard.gameBoard[X][Y] == 0:
                    print(negMessage.get(random.randint(0, 2)))
                    opponentBoard.gameBoard[X][Y] = 2  # pudlo
                    return False
                elif opponentBoard.gameBoard[X][Y] == 1:
                    print(posMessage.get(random.randint(0, 6)))
                    opponentBoard.gameBoard[X][Y] = 3  # trafiony
                    if opponentBoard.checkIfSunk(X, Y):  # trafiony-zatopiony
                        opponent.aliveShips -= 1
                    return True
                success = True
