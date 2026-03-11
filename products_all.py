products = []

def new_product():
    name = input("Enter product name: ")
    price = int(input("Enter the unit price of the product: ").replace(",","").replace(".","")) #I used int because if I put it in float and the user
    #enters a price with a . (meaning it's a thousand), it will be converted to a decimal, e.g., 2.000 = 2.0. I used integer and to avoid
    #errors, I replaced the , and . (in case they enter nothing, i.e., an empty space), I remove them before converting the number
    amount = int(input("Enter quantity: ")) #multiply the price by the quantity
    total = price * amount

    new_products = { #dictionary where I'm saving the info
        "name" : name,
        "price" : price,
        "amount" : amount,
        "total" : total
    }

    products.append(new_products) #Here I am sending them to the list

    print("=" * 34) #Here I print the CURRET product
    print(f"Name: {name:>27}")
    print(f"Price: ${price:>25,.0f}")
    print(f"Amount: {amount:>25}")
    print(f"Total: ${total:>25,.0f}")
    print("=" * 34)


def show_product(): #I display the history, a for loop to iterate through the entire list and display it
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
