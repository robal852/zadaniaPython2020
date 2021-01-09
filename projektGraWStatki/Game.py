from projektGraWStatki.Player import Player
from projektGraWStatki.Board import Board


class Game:
    """ Główna klasa reprezentująca gre w statki """

    def __init__(self):
        self.setUp()

    def setUp(self):
        """ Przygotowanie do rozgrywki, Wybor graczy i rozstawianie statkow
        player1, player2 - gracze
        board1, board2 - odpowiednio ich plansze ze statkami """

        print("Witaj w grze w statki!")
        self.choosePlayers()

        print("Teraz pora ustawić statki na planszy.")
        self.board1, self.board2 = Board(), Board()
        self.setBoard(self.player1, self.board1)
        self.setBoard(self.player2, self.board2)

        self.startGame()

    def choosePlayers(self):
        ''' Wybór czy gra człowiek czy komputer '''
        print("Wybierz graczy: wpisz 1 jesli czlowiek, wpisz 0 jesli komputer.")
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
                        "Jesli chcesz rozstawiac recznie wpisz 1, jesli chcesz by komputer zrobil to za ciebie wpisz 0: "))
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
        self.printGameStatus()
        while not self.isEnd():
            mv = True  # True gracz rusza, False zmiana kolejki, za trafienie jest dodatkowy ruch
            while (mv and not self.isEnd()):
                mv = self.player1.move(self.board2, opponent=self.player2)
                self.printGameStatus()
            mv = True
            while (mv and not self.isEnd()):
                mv = self.player2.move(self.board1, opponent=self.player1)
                self.printGameStatus()

    def isEnd(self):
        ''' Czy koniec gry'''
        if self.player1.isLoser() or self.player2.isLoser():
            print("KONIEC GRY!")
            return True
        return False

    def printGameStatus(self):
        ''' Podglad na stan gry'''

        print("Gracz 1:")
        self.board1.printBoard()
        print("Gracz 2:")
        self.board2.printBoard(
            visibleShips=False)  # Zakladam ze chce grac jako gracz 1 a gracz 2 to moj przeciwnik wiec nie bede podgladfal gdzie sa statki


print("Najlepiej wybrac gracz 1 jako czlowiek i gracz 2 jako komputer,\n"
      " bo ustawione, ze widac statki gracza 1, a gracza 2 sa niewidoczne.\n")
Game()
