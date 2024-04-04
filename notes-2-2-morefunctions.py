# More Functions
# Edan was Here :)
# April 4th

# Multiply Strings
greeting = "hello "

print(greeting * 2)

print("The quick brown fox jumps over the lazy dog.\n" * 2)

def stars(num_stars: int) -> str:
    value = ""

    # if value == 0 or value == 1
    #if value > 1 "*" * num_stars
    # else negative number -> error   

    if num_stars == 0 or num_stars == 1:
        value ="*"
    elif num_stars > 1:
        value = "*" * num_stars
    else:
        value = "ERROR"

print(stars(1))
print(stars(10))