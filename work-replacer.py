# Work Replacer
# Author: Edan
# Feb 26th


ask = input("Type 'noodles' or '100'\n").strip("!?.,").lower()

# Create a function called translate that accepts a string and replaces certain text
def translate(tr):
    if tr in ["hundred", "100", "a_hundred",]:
        return ("💯")
    elif tr in ["noodles", "noodle",]:
        return ("🍜")
    elif tr in ["hundrednoodles", "ahundrednoodles", "a_hundred_noodles", "hundred_noodles",]:
        return ("💯🍜")



def main(ma):
    print(translate(ask))

main(ask)