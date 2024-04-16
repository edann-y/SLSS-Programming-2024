# Classes and Objects


import time

# Big Ideas:
# Classes allow us to couple data and functions together
# Objects are the ACTUAL representation of the classes

# Create a Pokemon Class; this represents a pokemon 

class Pokemon: # Use a capital letter for class name
    def __init__(self):
        """A special method (function) called the Constructor. Contains all the properties/variables that describe a Pokemon."""
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "normal"
        self.actual_cry = "Squeal"

        print("A new Pokemon is born!")

    def cry(self) -> str:
        """Represents the sound a pokemon makes
        
        Returns:
            - string representing the sound it makes"""
        return f"{self.name}: {self.actual_cry}"
    
    def eat(self, food: str) -> str:
        """Represents feeding the Pokemon
        
        Params: 
            - food: what you feed it
            
        Return:
            - what it says after eating it"""
        
        if food.lower() == "berry":
            return f"{self.name} ate the berry."
        elif food.lower() == "potion":
            return f"{self.name} consumed the potion and feels healthier!"
        else:
            return f"{self.name} batted the {food} away."
        
        
class Wooper(Pokemon):
    def __init__(self):
        # Call constructor of Parent class
        super().__init__()

        


# Create two Pokemon using our class

# Make Wooper and Psyduck

pokemon_one = Pokemon()

#Change some properties in pokemon_one

pokemon_one.name = "Wooper"
pokemon_one.id = 194
pokemon_one.weight = 8.5
pokemon_one.height = 0.4
pokemon_one.type in ["Water", "Ground"]
pokemon_one.actual_cry = "*Squeal*"


pokemon_two = Pokemon()

pokemon_two.name = "Psyduck"
pokemon_two.id = 54
pokemon_two.weight = 19.6
pokemon_two.height = 0.8
pokemon_two.type = "Water"
pokemon_two.actual_cry = "Quack-wack"

# Printing Pokemon Info

# print(pokemon_one.name)
# print(pokemon_one.id)
# print(pokemon_one.weight)
# print(pokemon_one.height)
# print(pokemon_one.type)
# print(pokemon_one.actual_cry)

# print(pokemon_two.name)
# print(pokemon_two.id)
# print(pokemon_two.weight)
# print(pokemon_two.height)
# print(pokemon_two.type)
# print(pokemon_two.actual_cry)

# Testing Eat Method

print(pokemon_one.eat("berry"))
time.sleep(0.8)
print(pokemon_one.eat("potion"))
time.sleep(0.8)
print(pokemon_one.eat("chilan berry"))
