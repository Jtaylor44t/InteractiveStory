import time
import random

playerinventory = {}

wargear = {"Great Sword": 30, "Broadsword": 15, "Claymore": 40,}

magegear = {"Elder Staff": 50, "Wizard's Staff": 40, "House Staff": 35}

rangegear = {"Wood Bow": 20, "Long Bow": 30, "Mystical Bow": 45}

def checkinv():
    if input == ("checkinv"):
        print(playerinventory)

def playerstats():
    if advclass == 'Warrior':
        Attack = 10
        Max_Health = 50





print()
print("Welcome to A Knight's Adventure.")
print()
time.sleep(3)

print("An interactive story.")
print()
time.sleep(3)

print("Let's begin...")
print()
time.sleep(3)

global name 
name = input("Adventurer, what is your name?: ")
print()

global advclass 
advclass = input("Choose your Adventurer's class (Warrior, Mage, or Archer): ")
print()

print(f"Ahh...{advclass}...a fine choice indeed. You have a long road ahead of you {name}. Talos guide you.")
print()
time.sleep(5)

print("You awake in a tower and descend down the spiral staircase...")
print()
time.sleep(3)

print("You find a chest with weapons inside. Select your weapon")
print()
time.sleep(3)

#elif advclass == 'Warrior':
    #print("You find a chest outside of the tower. It contains a sword, armor, and a shield.")
if advclass == 'Warrior'.lower():
    print("Choose your weapon:")
    print("1) Great Sword: 30 Attack")
    print("2) Broadsword: 15 Attack")
    print("3) Claymore: 40 Attack")
    op1 = input()
    if op1 == '':
        playerinventory.append()
    print()
    time.sleep(3)

#elif advclass == 'Mage':
    #print("You find a chest outside of the tower. It contains wizard robes, a wizard cap, and a magical staff.")
if advclass == 'Mage'.lower():
    print("Choose your weapon:")
    print("1) Elder Staff: 50 Attack")
    print("2) Wizard's Staff: 40 Attack")
    print("3) House Staff: 35 Attack")
    op1 = input()
    if op1 == '':
        playerinventory.append()
    print()
    time.sleep(3)

#elif advclass == 'Archer':
    #print("You find a chest outside of the tower. It contains green dragonhide armor, 150 arrows, and a bow.")
if advclass == 'Archer'.lower():
    print("Choose your weapon:")
    print("1) Wood Bow: 20 Attack")
    print("2) Long Bow: 30 Attack")
    print("3) Mystical Bow: 45 Attack")
    op1 = input()
    if op1 == '':
        playerinventory.append()
    print()
    time.sleep(3)
    
print("You stop for a moment to observe your surroundings...")
print()
time.sleep(5)

print("After checking your surroundings, you hear a scream in the distance...")
print()
time.sleep(3)

print("Now you have a decision to make...")
print()
time.sleep(3)

print("1) Continue down the road.")  #main sequence
print("2) Venture into the forest.") #main sequence
op1 = input()

#Pressing 1:
def op1input1():
    print("You walk down the road. Unsure of where exactly you are.")
    print()
    time.sleep(3)
    print("You see a mysterious figure on the side of the road. He notices your equipment.")
    print()
    time.sleep(3)
    print("Mysterious Figure: Hello there stranger, are you a soldier?")
    print()
    time.sleep(3)
    print(f"1) (Lie) Yes I am. My name is {name} of the royal guard")
    print("2) What's it to you?")
    print(f"3) No I am not a soldier. My name is {name}. I woke up in a random tower a couple miles down the road.")
    op2 = input()
    print()
    time.sleep(3)
    if op2 == '1':
        print(f"Mysterious Figure: Well {name}, you are a long way from home. The nearest military base is a few dozen miles away")
        print()
        time.sleep(3)
        print(f"{name}: Well looks like I'll be heading that way. Thank you for the direction")
        print()
        time.sleep(3)
        print("Mysterious Figure: Stop talking.")
        print()
        time.sleep(3)
        print("(You continue walking down the road towards the military base knowing you aren't actually a soldier.)")

    if op2 == '2':
        print("Mysterious Figure: No need to be rude. Just trying to figure out why you are out here.")
        print()
        time.sleep(3)
        print("(You have upset the mysterious figure)")
        print()
        time.sleep(3)
        print(f"{name}: I don't see how that is your business. I think I will be going now.")
        print()
        time.sleep(3)
        print("Mysterious Figure: Not if I have anything to say about that!")
        print()
        time.sleep(3)
        print("(Mysterious Figure stands up and draws a sword.)")
        print()
        time.sleep(3)
        print("Mysterious Figure: Never should of come here!")
        print()
        time.sleep(3)

        if advclass == 'Warrior':
            input1 = input("Draw your sword?(y/n): ")
            if input1 == 'y':
                print("You draw your sword. The Mysterious Figure flees in terror.")
                print()
                time.sleep3
            if input1 == 'n':
                print("You flee from the Mysterious Figure. Deciding it is unwise fighting in an unknown land.")
                print()
                time.sleep3
        if advclass == 'Mage':
            input2 = input("Cast a spell?(y/n):")
            if input2 == 'y':
                print("You cast a spell, temporarily freezing the Mysterious Figure in place. Just long enough for you to get away.")
                print()
                time.sleep3
            if input2 == 'n':
                print("You drink a potion of invisibility. You run down the road while the Mysterious Figure tries to determine your whereabouts.")
                print()
                time.sleep3
        if advclass == 'Archer':
            input3 = input("Draw an arrow?(y/n): ")
            if input3 == 'y':
                print("You draw an arrow, the Mysterious Figure respects your range advantage and backs down.")
                print()
                time.sleep3
            if input3 == 'n':
                print("You flee from the Mysterious Figure. Not wanting to cause any more issues.")
                print()
                time.sleep3
        

    if op2 == '3':
        print("Mysterious Figure: How did you end up way out here? I haven't seen you around these parts before.")
        print()
        time.sleep(3)
        print(f"{name}: I woke up in a tower a little ways down the road. I found all of this gear in a chest outside. I don't remember how I got here.")
        print()
        time.sleep(3)
        print("Mysterious Figure: I saw a woman coming from that way yesterday. She was in a hurry.")
        print()
        time.sleep(3)
        print(f"{name}: You did? What did she look like?")
        print()
        time.sleep(3)
        print("Mysterious Stranger: Honestly I didn't get a great look at her. Her face was mostly covered.")
        print()
        time.sleep(3)
        print(f"{name}: Thanks stranger, maybe someone else has seen her in that direction. I'll check it out.")
        print()
        time.sleep(3)
        print("To be continued in the next chapter...")


if op1 == '1':
    op1input1()


print("(After your adventure, you return back to your original goal of figuring out where you are...)")
print()
time.sleep(3)








