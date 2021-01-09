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
                print("Ruch komputera")
                time.sleep(2)
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
