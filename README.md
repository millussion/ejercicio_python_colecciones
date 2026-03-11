# INVENTORY

The solution was divided into multiple modules to organize the code and separate responsibilities:

* *`main.py`* : The main script controls the program flow. It displays a welcome message and runs a loop that allows the user to continuously register products. The loop stops only when the user decides to exit the program.
  
* *`products_all.py`* : The product registration logic is handled in the **products_all module**. In this module, the program asks the user for the product name, unit price, and quantity. The price input is cleaned using *`replace()`* to remove commas and periods so it can be safely converted to an integer to then convert it into a thousand in a print Then the total sale value is calculated by multiplying the price by the quantity.
  Each product is stored in a single **dictionary** containing the product name, price, quantity, and total. These things are appended to a list called *`products`*, which acts as the storage for all sales made during the day.
  
* *`history.py`* : The **history module** is responsible for displaying the sales summary. It calculates the total amount collected during the day using the *`sum()`* function of python and iterates through the *`products`* list to display each recorded sale.

This structure improves readability and organization by separating the responsibilities of the program into different files: the main execution flow, the product management logic, and the sales history summary.

# flow chart:
![Diagrama sin título](https://github.com/user-attachments/assets/77abaab2-a2af-4a9b-8bf8-b6d8fac3420c)
