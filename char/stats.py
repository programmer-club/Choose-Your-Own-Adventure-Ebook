from random import randint


class Stats:
    def __init__(self, STR, CON, DEX, INT, WIS, CHA):
        self.STR = STR
        self.CON = CON
        self.DEX = DEX
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA


def pc_roll():
    # roll for each of 6 stats
    results = []
    for i in range(6):
        # roll 4 dice
        dice = []
        for j in range(4):
            dice.append(randint(1, 6))
        # discard lowest die
        dice.sort()
        del dice[0]
        # sum up all the remaining dice
        total = 0
        for die in dice:
            total += die
        # store total
        results.append(total)
    return results


def random_monster(level):
    # TODO: generate random stats appropriate for level
    pass


def mod(stat):
    return (stat - 10) // 2
