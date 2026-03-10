from productos import *


def history():
    total_day = sum(product["total"] for product in products)
    
    print("-" * 34)
    print("Sales history of the day".center(35))
    show_product()
    print(f"Total Day: ${total_day:>21,.0f}")

    