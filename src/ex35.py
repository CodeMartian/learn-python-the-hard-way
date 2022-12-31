from sys import exit

def gold_room():
    print(f"This room is full of gold! How much do you try to take?")
    
    choice = input("> ")
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man learn to type a number.")
    
    if how_much < 50:
        print(f"Nice, you're not too greedy and exit safely with {how_much} gold.")
    else:
        dead("You greedy bastard! You're too heavy to outrun the bear now! It tackles and mauls you.") 
    
def bear_room():
    print("There is a sleeping bear here.")
    print("The bear is sleeping in front of the gold room.")
    print("There is some honey in the corner of the room.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear notices you trying to take the honey and slaps your face off.")
        elif choice == "move honey" and not bear_moved:
            print("The bear notices the honey has moved, and goes to lay beside it.")
            bear_moved = True
        elif choice == "move honey" and bear_moved:
            dead("The bear sees you moving the honey and eats your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "open door" and not bear_moved:
            dead("You try to climb over the bear but it wakes up and tears you to pieces!")
        else:
            print("That is an invalid action.")
        
def cthulhu_room():
    print("You've opened the door to a different dimension of time and space. The Great Cthulhu awaits your presence.")
    print("As Cthulhu stares at you, you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    if "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "You're now dead.")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There are two doors to choose from.")
    print("Do you choose the left door or the right door?")

    choice = input("> ")
    if "left" in choice:
        bear_room()
    elif "right" in choice:
        cthulhu_room()
    else:
        dead("You wander the room and go insane until you starve.")


start()