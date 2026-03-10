from productos import *
from history import *

print("-" * 34)
print("Welcome to the ABC Inventory".center(33))
print("-" * 34)
running = True #varibale con valor booleano para no usar while true (︺︹︺)

while running:

    new_product()
    exit = input("Do you wanna exit? (Y/N): ").lower()

    if exit == "y":
        history()
        print("\nHave a nice rest of the day!")
        print("Exiting...")
        running = False 

