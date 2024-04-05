# Loops and Iterations
# Edan was Here :)
# April 5th

# Makin a grocery list

import time

grocery_list = ["blueberry muffins", "potato chips", "milk", "eggs", "orange juice", "AMD Radeon RX 6800 XT"]

for item in grocery_list:
    # Skip the rest of the list
    # If we get to "AMD Radeon RX 6800 XT"
    if item.lower() == "amd radeon rx 6800 xt":
        break
    print(f"* {item}")


# Use a loop to count to 100

for i in range(100):
    time.sleep(0.8)
    print(i + 1)
    