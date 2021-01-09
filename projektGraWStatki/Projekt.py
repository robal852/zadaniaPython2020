class setUp():
    """ Przygotowanie do rozgrywki
    player1, player2 - gracze
    board1, board2 - odpowiednio ich plansze ze statkami """

    def __init__(self):
        ''' Wybor graczy i rozstawianie statkow'''
        print("Witaj w grze w statki!")
        self.choosePlayers()

        print("Teraz pora ustawić statki na planszy.")
        self.board1, self.board2 = Board(), Board()
        self.setBoard(self.player1, self.board1)
        self.setBoard(self.player2, self.board2)
        #self.board1.printBoard()

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
            s = -1
            while (s != 0 and s != 1):
                try:
                    s = int(input(
                        "Jesli chcesz rozstawiac recznie wpisz 1, jesli chcesz by komputer zrobil to za ciebie wpisz 0: "))
                except ValueError:
                    print("Wpisz poprawnie! 1 lub 0")
            if (s):
                board.setBoardManually()
            else:
                board.setBoardAutomatic()
        else:
            board.setBoardAutomatic()


class Game:
    """ Główna klasa reprezentująca gre w statki """

    def __init__(self):
        setUp()

    def startGame(self):
        ''' Tu rozgrywka '''

        while (self.isEnd()):
            self.player1.move()
            self.player2.move()
        pass

    def isEnd(self):
        ''' Czy koniec gry'''
        pass


class Player:
    """ Klasa reprezentująca gracza (czlowiek lub komputer)"""

    def __init__(self, isHuman, board=None):
        """ isHuman true to czlowiek, false to komputer
            board - plansza na której gracz rozstawia swoje statki,"""
        self.isHuman = isHuman
        # self.board = board.setBoard()

    def __str__(self):
        if self.isHuman:
            return "Czlowiek"
        else:
            return "Komputer"

    def move(self):
        ''' Ruch czlowieka lub komputera '''
        if self.isHuman():
            pass
        else:
            pass


class Board:
    """ Klasa reprezentująca planszę do gry (10x10) """

    def __init__(self, warships=None, shoots=None):
        ''' Plansza zawiera statki i historie gdzie zostal ooddany strzal '''
        self.warships = warships
        self.shoots = shoots

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

    def setBoardAutomatic(self):
        ''' Ustawianie automatyczne dla komputera lub dla leniwego '''
        pass

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


class Warship:
    """ Klasa reprezentująca statek, który będzie na planszy """

    def __init__(self, x, y, size):
        ''' x, y - wspolrzedne zaczepienia statku
            size - dlugosc statku'''
        self.x = x
        self.y = y
        self.size = size


Game()
