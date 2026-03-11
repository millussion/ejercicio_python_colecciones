from products_all import *


def history():
    total_day = sum(product["total"] for product in products) #with the function of python sum im adding all the totals of every product
    print("-" * 34)
    print("Sales history of the day".center(35)) #center is for center
    show_product() #here i'm showing the function
    print(f"Total Day: ${total_day:>21,.0f}")

    
