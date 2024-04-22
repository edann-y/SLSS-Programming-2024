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
    def __init__(self, name="Wooper"):
        # Call constructor of Parent class
        super().__init__()

        # Assigning the default values to property
        self.name = name
        self.id = 194
        self.weight = 8.5
        self.height = 0.4
        self.type = ["Water", "Ground"]
        self.actual_cry = "*Squeal*"

    def hydro_pump(self, defender: Pokemon) -> str:
        """Simulate a hydro pump attack against another pokemon"""

        # Params:
        # - Defender = Defending Pokemon

        # Returns:
        #   Str representing the result of the attack

        response = f"{self.name} used Hydro Pump on {defender.name}!\n"

        is_resistant = False

        is_weak = False

        if type(defender.type) == list:
            for t in defender.type:
                if t.lower() in ["water", "grass", "dragon"]:
                    is_resistant = True
                    break
                if t.lower() in ["fire", "ground", "rock"]:
                    is_resistant = True
                    break
        elif type(defender.type) == str:
            if defender.type.lower() in ["water", "grass", "dragon"]:
                is_resistant = True
            if defender.type.lower() in ["fire", "ground", "rock"]:
                is_weak = True
        
        if is_resistant:
            time.sleep(1)
            response = response + "It was not very effective."

        if is_weak:
            time.sleep(1)
            response = response + "It was super effective!"

        return response
        

class Psyduck(Pokemon):
    def __init__(self, name="Psyduck"):
        # Call constructor of Parent class
        super().__init__()

        # Assigning the default values to property
        self.name = name
        self.id = 54
        self.weight = 19.6
        self.height = 0.8
        self.type = "Water"
        self.actual_cry = "Quack-wack"

    def confusion(self, defender: Pokemon) -> str:
        """Simulate a hydro pump attack against another pokemon"""

        # Params:
        # - Defender = Defending Pokemon

        # Returns:
        #   Str representing the result of the attack

        response = f"{self.name} used confusion on {defender.name}!\n"
        
        if defender.type.lower() in ["psychic", "steel"]:
            time.sleep(1)
            response = response + "It was not very effective."  

        return response
    
class Stunfisk(Pokemon):
    def __init__(self, name="Stunfisk"):

        super().__init__()

        self.name = name
        self.id = 618
        self.weight = 11
        self.height = 0.7
        self.type = ["Electric", "Ground"]
        self.actual_cry = "Bzzzt"

    def electroweb(self, defender: Pokemon) -> str:

        response = f"{self.name} used Electroweb on {defender.name}!\n"

        is_resistant = False

        is_weak = False

        is_immune = False

        if type(defender.type) == list:
            for t in defender.type:
                if t.lower() in ["electric", "grass", "dragon"]:
                    is_resistant = True
                    break
                elif t.lower() in ["water", "flying"]:
                    is_weak = True
                    break
                elif t.lower() == "ground":
                    is_immune = True

        elif type(defender.type) == str:
            if defender.type.lower() in ["electric", "grass", "dragon"]:
                is_resistant = True
            if defender.type.lower() in ["water", "flying"]:
                is_weak = True     
            elif t.lower() == "ground":
                is_immune = True   

        if is_resistant:
            time.sleep(1)
            response = response + "It was not very effective."

        if is_weak:
            time.sleep(1)
            response = response + "It was super effective!"

        if is_immune:
            time.sleep(1)
            response = response + f"It doesn't affect {defender}"

        return response
    
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
time.sleep(1)

wooper_one = Wooper()
wooper_two = Wooper("Jolly")
psyduck_one = Psyduck()
psyduck_two = Psyduck("Naive")
stunfisk_one = Stunfisk()
stunfisk_two = Stunfisk("Modest")

print(wooper_one.hydro_pump(pokemon_two))
print(stunfisk_one.electroweb(pokemon_two))
print(wooper_one.hydro_pump(stunfisk_one))