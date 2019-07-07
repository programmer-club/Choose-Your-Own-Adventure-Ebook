class Stats:
    def __init__(self, STR, CON, DEX, INT, WIS, CHA):
        self.STR = STR
        self.CON = CON
        self.DEX = DEX
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA


def roll():
    pass


def mod(stat):
    return (stat - 10) // 2
