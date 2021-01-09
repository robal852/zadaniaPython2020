class Player:
    """ Klasa reprezentująca gracza (czlowiek lub komputer)"""

    def __init__(self, isHuman):
        """ isHuman true to czlowiek, false to komputer """
        self.isHuman = isHuman

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
