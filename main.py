from products_all import *
from history import * #we import all the functions from the other files

print("-" * 34) 
print("Welcome to the ABC Inventory".center(33))
print("-" * 34)
running = True #variable with boolean value to avoid using while true (︺︹︺)

while running:

    new_product() #function to add product. Form to enter product, dictionary and print current product.
    exit = input("Do you wanna exit? (Y for EXIT, any letter to continue): ").lower() #the variable for the break of the while loop.

    if exit in ["y", "yes", "si"]: #if the variable is yes, show the summary/history and total, then set running to false to break the loop.
        history()
        print("\nHave a nice rest of the day!")
        print("Exiting...")
        running = False 

