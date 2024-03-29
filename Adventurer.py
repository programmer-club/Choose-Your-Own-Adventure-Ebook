import random
import sys
import time


# Consider making at lease some of these arguments keyword-only for clarity.
def validate(prompt="Are you sure? (y/n) ", options=('y', 'n'), msg="Please enter a valid input. ", surecheck=False):
    while True:
        text = input(prompt)
        if text in options:
            if not surecheck or validate() == 'y':
                return text
        else:
            print(msg)


print("Python version info: ")
time.sleep(2)  # Can we have less of these? We don't need 82, surely...
print(sys.version_info)
time.sleep(2)
funny = [
    "Gluten Free", "100% awesomeness.", "Something will happen. Guaranteed.", "Making your computer coffee...",
    "Setting off nukes for fun...", "Destroying your computer...", "Opening a portal...",
    "Getting sprockets 97%... Finding user installler 99%... Done.", "Measuring the sun...", "Beep boop"
]
print(random.choice(funny))
time.sleep(2)
print("Hello! Welcome to the Programmer Club Gamebook Adventure Ebook, Adventurer v1, Python edition! Let's get"
      " started!")
time.sleep(2)
sure = validate("Do you want to see the credits? (y/n)", surecheck=True)
time.sleep(2)
while sure == "y":
    print()
    time.sleep(2)
    sure = validate("Would you like to replay the credits? (y/n)")
if sure != "y":
    time.sleep(2)
    print("Okay then.")
time.sleep(2)
sure = validate("Do you want to continue a game? (y/n)", surecheck=True)
if sure == "y":
    try:
        time.sleep(2)
        saves = open("saves.txt", "r")
        char_name = validate("Type again, then.", "", "Sorry, I could not find that name in your saves.")
        line = 1

        def nln():
            global line  # Global here resolves scope conflicts. Isaac- What?
            line += 1
        while save_name != char_name:  # save_name isn't defined either.
            save_name = saves.readline(line)
            nln()
        nln()
        hlth = saves.readline(line)
        nln()
        stre = saves.readline(line)
        nln()
        dex = saves.readline(line)
        nln()
        con = saves.readline(line)
        nln()
        inte = saves.readline(line)
        nln()
        cha = saves.readline(line)
        nln()
        luck = saves.readline(line)
        nln()
        defense = saves.readline(line)
        nln()
        hp = saves.readline(line)
        nln()
        cash = saves.readline(line)
        nln()
        spell = saves.readline(line)
        nln()
        spellpwr = saves.readline(line)
    except OSError:
        time.sleep(2)
        print("You don't have any saved games or you falsely put in the name.")
        time.sleep(2)
        print(">;)")
        time.sleep(2)
        print("I know if you're inputting falsely...")
        time.sleep(2)
        print("Anyway, sorry, you will have to play the game from the beginning.")
        sure = "n"
if sure != "y":
    time.sleep(2)
    print("Okay.")
    time.sleep(2)
    print("So, do you know what a gamebook is?")
    time.sleep(2)
    sure = validate("Tell me if you would like to know. (y/n)")
    if sure == "y":
        time.sleep(2)
        print("A gamebook is a usually a book where someone roleplays in a one-player game.")
        time.sleep(2)
        print("They make choices to do well and achieve their goal in the game.")
    time.sleep(2)
    print("Okay.")
    time.sleep(2)
    print("Moving along...")
    time.sleep(2)
    print("You need a character.")
    time.sleep(2)
    print("What should his/her name be?")
    time.sleep(2)
    print("If you use punctuation, it will appear in your character's name.")
    time.sleep(2)
    char_name = input("Don't use numbers.")
    time.sleep(2)
    sure = validate()
    if sure != "y":  # Never use is or is not for comparison between immutable objects.
        time.sleep(2)
        char_name = input("Type the name again, then.")
    time.sleep(2)
    char_gender = validate("Gender? (m/f)", ("m", "f"))
    time.sleep(2)
    sure = validate()
    if sure != "y":
        time.sleep(2)
        char_gender = validate(
            "Type {0}'s gender again, then.".format(char_name), ("m", "f"),
            "Sorry, that is not a valid input. Type again."
        )  # This is all in the name of readability...
    if char_gender == "m":
        he = "he"
        his = "his"
        him = "him"
    else:
        he = "she"
        his = "her"
        him = "her"
    time.sleep(2)
    print("So, we are gonna roll up", char_name, "now...")
    stre = random.randint(1, 6) + random.randint(1, 6) + 6
    dex = random.randint(1, 6) + random.randint(1, 6) + 6
    con = random.randint(1, 6) + random.randint(1, 6) + 6
    inte = random.randint(1, 6) + random.randint(1, 6) + 6
    cha = random.randint(1, 6) + random.randint(1, 6) + 6
    luck = random.randint(1, 6) + random.randint(1, 6) + 6
    defense = random.randint(1, 6) + random.randint(1, 6) + 6
    hp = random.randint(1, 10) + 10
    cash = random.randint(1, 55) + 40
    spell = random.randint(1, 55) + 25
    spellpwr = random.randint(1, 6) + random.randint(1, 6) + 6
    time.sleep(2)
    print("Here are", char_name + "'s stats:")
    time.sleep(2)
    print("Strength:", stre)
    time.sleep(2)
    print("Dexterity:", dex)
    time.sleep(2)
    print("Constitution:", con)
    time.sleep(2)
    print("Intelligence:", inte)
    time.sleep(2)
    print("Charisma:", cha)
    time.sleep(2)
    print("Luck:", luck)
    time.sleep(2)
    print("Defense:", defense)
    time.sleep(2)
    print("HP:", hp)
    time.sleep(2)
    print("Spell Points:", spell)
    time.sleep(2)
    print("Spell Power:", spellpwr)
    time.sleep(2)
    print("Cash:", cash)
    time.sleep(2)
    print("If you haven't played this before, you should probably learn the rules.")
    time.sleep(2)
    sure = validate("Would you like me to tell you? (y/n)")
    if sure == "y":
        time.sleep(2)
        print(
            "Okay. So, in this game, you have to choose different actions that are listed for you.")
        time.sleep(2)
        print("They determine the path and the survival of your character.")
        time.sleep(2)
        print("They also determine if {0} goals will be achieved, what goods they get, and more.".format(his))
        time.sleep(2)
        print("The choices will be numbered.")
        time.sleep(2)
        print("Also, you can input these things:")
        time.sleep(2)
        print("1. The number of a choice to choose it.")
        time.sleep(2)
        print("2. The command \"moo/Char\", to see your character's stats.")
        time.sleep(2)
        print("3. The command \"moo/8ball\", to give you a lucky choice.")
        time.sleep(2)
        print("4. The command \"moo/yn\", to give you a lucky choice between yes and no.")
        time.sleep(2)
        print(
            "5. The command \"moo/yn <number>, <number>\", to generate a random number between the two numbers"
            " inputted."
        )
        time.sleep(2)
        print("5. The command \"moo/Help\", to open this message.")
        time.sleep(2)
        print("6. The command \"moo/Save\", to save your game and character, and then exit.")
        time.sleep(2)
        print(
            "You currently cannot use these inputs.")
        time.sleep(2)
        print("When you start playing you can.")
        time.sleep(2)
        print("Now I will teach you how combat works.")
        time.sleep(2)
        print("First, you choose an opponent.")
        time.sleep(2)
        print("Then, you choose your weapon or spell, or you can also choose to punch. (Spells can only be casted if"
              " your character has enough mana to cast a spell.)")
        time.sleep(2)
        print("Then, if you are"
              " making an attack with a weapon or punching, you add a random range of 1 to 6 to another random range"
              " of 1 to 6, and then add your strength to that.")
        time.sleep(2)
        print("This is your attack score.")
        time.sleep(2)
        print("If you are making an attack with"
              " a spell, then your attack score is determined with your spell power, not your strength.")
        time.sleep(2)
        print("Then, if your"
              " attack score is higher than your opponent's defense, you attack and their HP gets deducted by your"
              " attack's attack power.")
        time.sleep(2)
        print("If not, nothing happens.")
        time.sleep(2)
        print("Then, if there is anyone else in your party, they go"
              " through the process in the order the party would have to be in.")
        time.sleep(2)
        print("Then, the opponents have their attack.")
        time.sleep(2)
        print("The battle cycles until one whole party gets eliminated or the battle ends some other way.")
        time.sleep(2)
        print("Battles"
              " change under different circumstances.")
        time.sleep(2)
        print("More will be explained later.")
        time.sleep(2)
        print("Now, will {0} be a warrior or spellcaster?")
        time.sleep(2)
        print("This will determine if {0} will do stuff like using"
              " weapons or punching (warrior) or casting spells and using potions (spellcaster).".format(char_name))
        classe = validate(
            "Tell me \"Warrior\" or" \"Spellcaster\".",
            ("\"Warrior\"", "\"Spellcaster\""), surecheck=True
        )
        time.sleep(2)
        print("Okay. You are going to have to choose your attacks.")
        time.sleep(2)
        print("The list that pops up will be determined by your class (warrior or spellcaster).")
        time.sleep(2)
        print("Under every attack is the price you will pay if you get it.")
        time.sleep(2)
        print("If you are a warrior you pay cash, and if you are a spellcaster you pay spell points.")
        time.sleep(2)
        print("You can get 3 attacks at the moment.")
        time.sleep(2)
        print("Your cash is " + str(cash) + ".")
        time.sleep(2)
        print("Also, just remember that your character already can punch and kick.")
        warrior = ["1*Battleaxe", "10", "1*Club", "0.1", "1, 4", "1*Crossbow", "30", "1, 5", "1*Dagger", "2", "1, 4",
                   "1*Dart", "0.05", "1, 4", "1*Flail", "10", "1, 8", "1*Glaive", "20", "1, 10", "1*Greatclub", "0.2",
                   "1, 8", "1*Halberd", "20", "1, 10", "1*Handaxe", "1", "1, 6", "1*Javelin", "0.5", "1, 6", "1*Mace",
                   "5", "1, 6", "2*Maul", "10", "1, 6", "1*Morningstar", "15", "1, 8", "1*Pike", "5", "1, 10",
                   "1*Rapier", "1, 8", "25", "1*Scimitar", "25", "1, 6", "1*Sickle", "1", "Sling", "0.1", "Spear", "1",
                   "Staff", "0.2", "Sword", "12", "Trident", "5", "War Pick", "5", "Warhammer", "15", "Whip", "2"]
        time.sleep(2)
        print("Yay, we have", char_name, "rolled up!")
        time.sleep(2)
        print("         _______")
        print("         |   ( /")
        print("        |    \\|")
        print(" ____   |_____|")
        print("(__________)  |")
        print("(__________)  /")
        print("(________(_| /")
        print("(________(_//")
        lvl = 1  # assuming lvl starts at 1?
        stats = "Name: {0}:Level{1} Focus: {2}".format(char_name, lvl, classe)
        print("Here is", his, "stats:", stats)
