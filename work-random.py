# Random Dice Game
# Author: Edan
# Mar 11th

# Importing 
import random
import time

# Greet and Introduce the game
print("Hello!")

time.sleep(1.5)

print("I'm the dice bot.")

time.sleep(1)

print("Let's play a game! We'll roll a dice and whoevers number is higher wins!")

time.sleep(1)

print("You roll yours first.")

time.sleep(0.5)

# Start the game
def main():
    roll = input("Please type 'roll' to roll the dice.\n").strip("?.,!").lower()

    while True:
        if "roll" in roll:
            print("Rolling...")
            break
        else:
            print("...")
            time.sleep(0.5)
            roll = input("Please type 'roll' to roll the dice.\n").strip("?.,!").lower()

    time.sleep(2)

    dice = random.randint(1,6)

    print(dice)

    time.sleep(1)

    print("Now it's my turn!")

    time.sleep(1.5)

    dicer = random.randint(1,6)

    print(dicer)

    if dice > dicer:
        print("Looks like I lost!")
    elif dice < dicer:
        print("I won! Yay!")
    elif dice == dicer:
        print("Looks like we tied.")    

def main2():
    roll = input("Please type 'roll' to roll the dice.\n").strip("?.,!").lower()

    while True:
        if "roll" in roll:
            print("Rolling...")
            break
        else:
            print("...")
            time.sleep(0.5)
            roll = input("Please type 'roll' to roll the dice.\n").strip("?.,!").lower()

    time.sleep(2)

    dice = random.randint(1,6)

    print(dice)

    time.sleep(1)

    print("Now it's my turn!")

    time.sleep(1.5)

    dicer = random.randint(1,6)

    print(dicer)

    if dice > dicer:
        print("Looks like I lost!")
    elif dice < dicer:
        print("I won! Yay!")
    elif dice == dicer:
        print("Looks like we tied.")    

    print("Would you like to play again?")

    again = input("Input 'Yes or No'.\n").strip("?.,!").lower()

    while True:
        if again == "yes":
            main2()
        elif again == "no":
            print("Ok! I had fun. See you next time!")
            break
        else: 
            print("...")
            time.sleep(0.5)
            again = input("Input 'Yes or No'.\n").strip("?.,!").lower()

main()

time.sleep(2)

print("That was fun!")

time.sleep(1)

print("Would you like to play again?")

again = input("Input 'Yes or No'.\n").strip("?.,!").lower()

while True:
    if again == "yes":
        main()
    elif again == "no":
        print("Ok! I had fun. See you next time!")
        break
    else: 
        print("...")
        time.sleep(0.5)
        again = input("Input 'Yes or No'.\n").strip("?.,!").lower()





