# McDonald's Bot
# Author: Edan
# Feb 22nd

# Greet the user and ask them what they want
print("Hi there! What can I get for you")

order = input("Menu:\n Big Mac \n Cheeseburger \n McMuffin \n").lower().strip("!.?,")

# Take their order
if order == "big mac":
    print("For sure!")
elif order == "cheeseburger":
    print("For sure!")
elif order == "mcmuffin":
    print("For sure!")
else:
    print("Uhh alright.")


# Add on to their order
    print("Would you like fries with that? It's a free promotion for today.")

fries = input("Enter Yes or No \n").lower().strip("!.?,")
    
# Take their answer
if fries == "yes":
    print("Alright.")
elif fries == "no":
    print("No? Alright.")
else: 
    print("I'm not sure I understand but i'll take it as a no.")


# Ask them if they want a drink
    print("Would you like a drink along with your order?")

drink = input("Enter Yes or No \n").lower().strip("!.?,")
    
# Take their answer
if drink == "yes":
    print("Spot on!")
elif drink == "no":
    print("No? Alright.")
else: 
    print("I'm not sure I understand but i'll take it as a no.")


