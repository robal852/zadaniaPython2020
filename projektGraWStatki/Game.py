from Player import Player
from Board import Board
from os import system, name
import random


class Game:
    """ Główna klasa reprezentująca gre w statki """

    def __init__(self):
        """ Przygotowanie do rozgrywki, Wybor graczy i rozstawianie statkow
        player1, player2 - gracze
        board1, board2 - odpowiednio ich plansze ze statkami """

        print("Witaj w grze w statki!")
        self.choosePlayers()

        print("Teraz pora ustawić statki na planszy.")
        self.board1, self.board2 = Board(), Board()
        self.setBoard(self.player1, self.board1)
        self.setBoard(self.player2, self.board2)

        # self.startGame()

    def choosePlayers(self):
        ''' Wybór czy gra człowiek czy komputer '''
        print(
            "Wybierz graczy: wpisz 1 jesli czlowiek, wpisz 0 jesli komputer.")
        p1, p2 = -1, -1
        while (p1 != 0 and p1 != 1):
            try:
                p1 = int(input("Wybierz dla  Gracz 1 : "))
            except ValueError:
                print("Wpisz poprawnie! 0 lub 1")
        while (p2 != 0 and p2 != 1):
            try:
                p2 = int(input("Wybierz dla  Gracz 2 : "))
            except ValueError:
                print("Wpisz poprawnie! 0 lub 1")

        self.player1 = Player(bool(p1))
        self.player2 = Player(bool(p2))
        print("Wybrano:")
        print("Gracz 1: ", self.player1)
        print("Gracz 2: ", self.player2)

    def setBoard(self, player, board):
        ''' Rozstawianie statkow na planszy
         komputer - automatycznie
         czlowiek - ma mozliwosc wyboru czy sam czy automatycznie'''
        if (player.isHuman):
            choice = -1
            while (choice != 0 and choice != 1):
                try:
                    choice = int(input(
                        "Jesli chcesz rozstawiac recznie wpisz 1, "
                        "jesli chcesz by komputer zrobil to za ciebie wpisz "
                        "0: "))
                except ValueError:
                    print("Wpisz poprawnie! 1 lub 0")
            if (choice):
                board.setBoardManually(player)
            else:
                board.setBoardAuto(player)
        else:
            board.setBoardAuto(player)

    def startGame(self):
        ''' Tu rozgrywka '''

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

        self.printGameStatus()
        while not self.isEnd():
            mv = True  # True gracz rusza, False zmiana kolejki,
            # za trafienie jest dodatkowy ruch
            while (mv and not self.isEnd()):
                mv = self.player1.move(self.board2, opponent=self.player2)
                self.printGameStatus()
                if self.player1.isHuman:
                    if mv:
                        print(posMessage.get(random.randint(0, 6)))
                    else:
                        print(negMessage.get(random.randint(0, 2)))
            mv = True
            while (mv and not self.isEnd()):
                mv = self.player2.move(self.board1, opponent=self.player1)
                self.printGameStatus()
                if self.player2.isHuman:
                    if mv:
                        print(posMessage.get(random.randint(0, 6)))
                    else:
                        print(negMessage.get(random.randint(0, 2)))

    def isEnd(self):
        ''' Czy koniec gry'''
        if self.player1.isLoser():
            print("KONIEC GRY!")
            print("WYGRAL GRACZ 2")
            return True
        elif self.player2.isLoser():
            print("KONIEC GRY!")
            print("WYGRAL GRACZ 1")
            return True
        return False

    def printGameStatus(self):
        ''' Podglad na stan gry
        Czyszci terminal, po czym wypisuje aktualne plansze graczy
        '''

        # https://www.geeksforgeeks.org/clear-screen-python/
        # for windows
        if name == 'nt':
            _ = system('cls')
            # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

        print("Gracz 1:")
        self.board1.printBoard()
        print("\nGracz 2:")
        self.board2.printBoard(
            visibleShips=False)  # NIE WIDZE STATKOW GRACZA 2
