# String Methods
# Author: Edan Yu
# Feb 22nd

# Ask the user what is the weather like
weather = input("What's the weather like? ")

# If they reply with "rainy"
 # Advise them to bring an umbrella
if weather.lower().strip("!.?,") == "rainy":
    print("That's not good! Make sure to bring an umbrella to keep yourself dry ☂ ")
else: 
    print("Sorry, I don't understand.")