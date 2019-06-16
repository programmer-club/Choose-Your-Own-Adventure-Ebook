import random
print(__import__('sys').version_info)
print("Copyright Programmer's Club. DO NOT DISTRIBUTE")
print("Hello! Welcome to the Programmer's Club's Choose-Your-Own Adventure Ebook! Let's get started!")
understand = input("So, do you know what a choose-your-own adventure is? Tell me if you would like to know. y/n")
if understand is "y":
    print("A choose-your-own adventure game is a usually a game where someone roleplays in a one-player game. They make choices to do well and achieve their goal in the game.")
print("Okay. Moving along...")
char_name = input("You need a character. What should his/her name be? If you use punctuation, it will appear in your player's name.")
sure = input("Are you sure? y/n")
if not sure is "y":
    char_name = input("Type the name again, then.")
char_gender = input("Gender?")
if not sure is "y":
    char_name = input("Type your character's gender again, then.")
print(("So, we are gonna roll up") + int(char_name) + "now...")
stre = random.randint(1, 6) + (1, 6) + 6
dex = random.randint(1, 6) + (1, 6) + 6
con = random.randint(1, 6) + (1, 6) + 6
inte = random.randint(1, 6) + (1, 6) + 6
cha = random.randint(1, 6) + (1, 6) + 6
luck = random.randint(1, 6) + (1, 6) + 6
hp = random.randint(1, 10) + 10
print("Here is your" + int(char_name) + ": Strength: " + int(stre) + "Dexterity: " + int(dex) + "Consitution: " + int(con) + "Intelligence: " + int(inte) + "Charisma: " + int(cha) + "Luck: " + int(luck) + int(upper(hp)) + ": " + int(hp))