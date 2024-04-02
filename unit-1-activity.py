# Unit 1 Activity
# Author: Edan
# Mar 5th

# Greet the user
print("Hi!")

print("I'm the demonstrator bot, to demonstrate Edan's skills this unit.")

# Conditionals
print("Now tell me, what do you like to do on your free time?")

free_time = input("What do you do in your free time \n").strip("!?.,")

print("Oh that's cool!")

print("What do you like to eat?")

food = input().strip("!?.,").lower()

print(f"Siiiiick! I like {food} too! It's not my favourite though.")

# String Methods

print("Do you like math?")

like = input("Input 'Yes' or 'No'.\n").strip("!?.,").lower()

if like == "yes":
    print("That's awesome! I'm gonna do some!")
elif like == "no":
    print("Well too bad, I'm gonna do some anyways")

# Functions
print("Let me do some 'quick math!' -Big Shaq")

print("Give me any number i'll do addition, subtraction, division, and multipication with a decimal place!")

def main():
    add = math(input("Please input a number.\n"))
    sub = maths(input("Please input a number.\n"))
    multi = mathz(input("Please input a number.\n"))
    divi = mathing(input("Please input a number.\n"))
    total = add - sub * multi / divi

    print(f"Your final number is {round(total, 1)}")

def math(x: int):
    return float(x)


def maths(x: int):
    return float(x)


def mathz(x: int):
    return float(x)


def mathing(x: int):
    return float(x)


main()

print("Well, that's all I have tasked for today. Bye!")

