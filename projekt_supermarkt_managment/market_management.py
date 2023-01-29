#Aufgabe 4
import pandas as pd
from supermarket import *

products_pd = pd.read_csv("products.csv", sep=";")
employees_pd = pd.read_csv("employees.csv", sep=";")

column_products = ["Name", "Prod_id", "Category", "PRICE"]
prod = products_pd[[*column_products]]
products = list(prod.to_records(index = False))
column_employees = ["Name", "Age", "Pers_id", "JOB_ID"]
emplo = employees_pd[[*column_employees]]
employees = list(emplo.to_records(index = False))


from supermarket import Supermarket, Product, Employee
my_supermarket = Supermarket("Supermarket Deluxe", "Marienplatz 1", "München")
my_supermarket.products = [Product(*item) for item in products]
my_supermarket.employees = [Employee(*item) for item in employees]


#Aufgabe 6
print(f'Supermarket Deluxe hat {len(my_supermarket.employees)} Mitarbeiter.')

def expensive_product(prod_list):
    max_price = None
    max_prod_position = ""
    for i, prod in enumerate(prod_list):
        if not max_price or max_price <= prod.price:
            max_price = prod.price
            max_prod_position = i
    return prod_list[max_prod_position]

most_expensive_product = expensive_product(my_supermarket.products)
print(f'Das teuerste Produkt ist {most_expensive_product.name}.')

import statistics
avg_price = statistics.mean([prod.price for prod in my_supermarket.products])
avg_price = round(avg_price, 2)
print(f'Im Durchschnitt kostet ein Produkt {avg_price:.2f}€.')

from collections import Counter
category_counter = Counter([prod.category for prod in my_supermarket.products])
print(f'Die Produkte sind wie folgt aufgeteilt: {category_counter}')