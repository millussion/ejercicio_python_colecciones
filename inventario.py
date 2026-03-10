from productos import *
from history import * #importamos todas las funciones de los otros archivos

print("-" * 34) #decoración repite el guión medio - 34 veces
print("Welcome to the ABC Inventory".center(33))
print("-" * 34)
running = True #varibale con valor booleano para no usar while true (︺︹︺)

while running: #mientras running sea verdadero se va a ejecutar.

    new_product() #función para agregar producto. Formulario para ingresar prod. el diccionario y el print del actual producto.
    exit = input("Do you wanna exit? (Y/N): ").lower() #la variable para el break del while.

    if exit == "y": #si la variable es y de yes muestra el resumen/historial y total para luego definir running como false para romper el bucle.
        history()
        print("Have a nice rest of the day!")
        print("Exiting...")
        running = False 

