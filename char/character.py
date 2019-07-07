from .stats import random_monster


class Character:
    def __init__(self, gender=None, name="Slime", classType="Monster", level=1, stats=None):
        self.gender = gender
        self.name = name
        self.classType = classType
        self.level = level
        if stats:
            self.stats = stats
        else:
            self.stats = random_monster(level)
