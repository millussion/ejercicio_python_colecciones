products = []

def new_product():
    name = input("Enter product name: ")
    price = int(input("Enter the unit price of the product: ").replace(",","").replace(".",""))
    amount = int(input("Enter quantity: "))
    total = price * amount

    new_products = { 
        "name" : name,
        "price" : price,
        "amount" : amount,
        "total" : total
    }

    products.append(new_products)

    print("=" * 34)
    print(f"Name: {name:>27}")
    print(f"Price: ${price:>25,.0f}")
    print(f"Amount: {amount:>25}")
    print(f"Total: ${total:>25,.0f}")
    print("=" * 34)


def show_product():
    if not products:
        print("There's not products")
    else :

        for product in products:
            print("=" * 34)
            print(f"Name: {product['name']:>27}"),
            print(f"Price: ${product['price']:>25,.0f}"),
            print(f"Amount: {product['amount']:>25}")
            print(f"Total: ${product['total']:>25,.0f}"),
            print("=" * 34)
