class Character:
    def __init__(self, gender, name, stats, classType='Monster', level=1):
        self.gender = gender
        self.name = name
        self.level = level
        self.stats = stats
        self.classType = classType
