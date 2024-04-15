# Classes and Objects

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

        print("A new Pokemon is born!")

# Create two Pokemon using our class

# Make Wooper and Psyduck

pokemon_one = Pokemon()

#Change some properties in pokemon_one

pokemon_one.name = "Wooper"
pokemon_one.id = 194
pokemon_one.weight = 8.5
pokemon_one.height = 0.4
pokemon_one.type in ["Water", "Ground"]


pokemon_two = Pokemon()

pokemon_two.name = "Psyduck"
pokemon_two.id = 54
pokemon_two.weight = 19.6
pokemon_two.height = 0.8
pokemon_two.type = "Water"

print(pokemon_one)