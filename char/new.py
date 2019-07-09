from .stats import pc_roll


def new():
    gender = validate("Choose your character's gender (m/f): ", ('m', 'M', 'f', 'F'))
    name = input("Type your character's name: ")
    # class system open to changes
    classType = validate("Now it's time to choose a class: " +
                         "If you choose the Warrior, " +
                         "you will be a close-range, high HP fighter that mainly uses simple melee attacks.\n" +
                         "The Warrior has less complex fights and is recommended for beginners.\n" +
                         "If you choose the Spellcaster, " +
                         "you will be a long-range, low HP fighter that mainly uses a variety of magic spells.\n" +
                         "The Spellcaster has more complex fights and is recommended for advanced players.",
                         ('warrior', 'Warrior', 'spellcaster', 'Spellcaster'))
    rolls = pc_roll()
    # TODO: allow players to arrange stats


def validate(prompt, options):
    while True:
        text = input(prompt)
        if text in options:
            return text
        else:
            print("Invalid input. Please choose one of the options available.")
