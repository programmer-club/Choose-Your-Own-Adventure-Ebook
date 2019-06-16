print(__import__('sys').version_info)
print("Copyright Programmer's Club. DO NOT DISTRIBUTE")
print("Hello! Welcome to the Programmer's Club's Choose-Your-Own Adventure Ebook! Let's get started!")
understand = input("So, do you know what a choose-your-own adventure is? Tell me if you would like to know. y/n")
if understand is "y":
    print("A choose-your-own adventure game is a usually a game where someone roleplays in a one-player game. They make choices to do well and achieve their goal in the game.")
else:
    print("Okay. Moving along...")
print("So, we are gonna roll up your character now.")
print("Here is your character: Strength:" + int() + "")