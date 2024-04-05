# Star Pyramid Exercise 
# Edan was Here :)
# April 5th 2024

def pyramid(base_width: int):
    """Prints a pyramid of stars of given base width"""
    # Params:
    #     base_width - bottom row of stars
    for i in range(base_width):
        print(stars(i + 1))

def stars(num_stars: int) -> str:
    value = ""

    # if value == 0 or value == 1 "*"
    # if value > 1 "*" * num_stars
    # else negative number -> error
    if num_stars == 0 or num_stars == 1:
        value = "*"
    elif num_stars > 1:
        value = "*" * num_stars
    else:
        value = "Sorry, can't take negative numbers."

    return value



pyramid(100)


