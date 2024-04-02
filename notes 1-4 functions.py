# Functions
# Author: Edan
# Feb 26th

# Create a function called say_hello
#   It's going to print "Hello"

def say_hello():
        print("Hello!")

# Create a function called say_hello_params
#  Print "Hello" {parameter}!?
#   ---> e.g say_hello_params("Jim!")
        
def say_hello_params(name):
        print(f"Hello, {name}!")



#       It returns how big the number is
def how_big(num):
    if num < 0:
        return "Very Small"
    if num < 10:
        return "Pretty Small"
    if num < 100:
        return "Small"
    if num < 1000:
        return "Big"
    if num < 10000:
        return "Pretty Big"
    if num < 100000:
        return "Very Large"
    

say_hello()
say_hello_params("Jim")
say_hello_params("🌎")


print(how_big(-1))
print(how_big(1))

result = how_big(1_000_000)
print(result)

def clean_input(prompt):
     return input(prompt).strip("!?.,")

# Create a function calle adder
#   Accepts two inputs that are numbers
#   Returns the SUM of both numbers

def adder(x: int, y: int):
     return x + y 

result = adder(1, 1)
print(result)
