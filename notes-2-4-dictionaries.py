# Notes - Dictionaries 

# Big Ideas:
# A dictionary is a data structure
# Dictionaries map keys to values

import time

# Flashback to lists

person = ["Bob", "64 years old", "likes apples"]

# Get and print the person's name(?)
print(person[0])
time.sleep(1)

# Print the full qualities

print(f"This person's name is "+person[0]+". He is "+person[1]+". Bob "+person[2]+".")
time.sleep(2)

print("person[2] will count the last item from the list") # Last item on list
time.sleep(1)
print("person[-1] will start counting from the end") # start counting from the end

time.sleep(1)

print("print(person[10])"+ " will break") # Code will break

time.sleep(1.5)

# Rewriting person as a dictionary

person_dictionary = {"name": "John", "age": "64 years old", "favourite_food": "apples"}

# Grab values from dictionary
print(person_dictionary["name"])
time.sleep(1)

for info in person_dictionary:
    print(info)

for key, value, in person_dictionary.items():
    print(key,value, sep=": ")