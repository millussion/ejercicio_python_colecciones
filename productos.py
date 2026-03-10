products = []

def new_product():
    name = input("Enter product name: ")
    price = int(input("Enter the unit price of the product: ").replace(",","").replace(".","")) #lo puse int pq al ponerlo en float y el usuario 
    #digitar un precio con un . haciendo entender que es un mil lo va a convertir en decimal ej: 2.000 = 2.0, lo puse entero y para que no haya 
    #errores reemplacé las , y . en caso de que llegue a digitarlo a nada osea "" vacio las elimino antes de convertir el numero
    amount = int(input("Enter quantity: "))
    total = price * amount #multiplico el precio por cantida

    if price == "":
        print("Error: you must enter a number.")
        return

    new_products = { #diccionario donde estoy guardando la info
        "name" : name,
        "price" : price,
        "amount" : amount,
        "total" : total
    }

    products.append(new_products) #aqui las estoy enviando a la lista

    print("=" * 34) #aqui imprimo el producto actual
    print(f"Name: {name:>27}")
    print(f"Price: ${price:>25,.0f}")
    print(f"Amount: {amount:>25}")
    print(f"Total: ${total:>25,.0f}")
    print("=" * 34)


def show_product(): #muestro el historial, un for para que recorra toda la lista y la muestre
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
