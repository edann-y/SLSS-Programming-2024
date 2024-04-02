# Tip Bot
# Author: Edan
# Feb 29th

def main():
    dollars = dollars_to_float(input("How much was the meal?\n"))
    percent = percent_to_float(input("What percentage would you like to tip?\n"))
    tip = dollars * percent


    # Note: This is one way to round a number to two decimal places
    print(f"Leave ${round(tip, 2)}")

def dollars_to_float(d):
    # Converts string dollars to a decimal float
    #    Returns the result
    # TODO
    return float(d) / 1.00


def percent_to_float(p):
    # Converts percent to a decimal float
    #    Returns the result
    # TODO
    return float(p) / 100

main()