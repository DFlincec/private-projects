#Aufgabe 1
class Supermarket:
    
    def __init__(self, name, street, city):
        self.name = name.title()
        self.street = street.title()
        self.city = city.title()
        self.employees = []
        self.products = []
        
#Aufabe 2
from datetime import *
now = datetime.now()
current_time = now.strftime("%H:%M")

class Employee():
    
    def __init__(self, name, age, pers_id, job):
        self.name = name.title()
        self.age = age
        self.pers_id = pers_id
        self.job = job.title()
        
    def greet_customer(self):
        print(f'Guten Tag. Mein Name ist {self.name} und ich bin {self.job} in diesem Supermarkt. Es ist momentan {current_time} Uhr - wie kann ich Ihnen helfen?')
        
    def celebrate_birthday(self):
        self.age += 1
        print(f'Juhu! Heute werde ich {self.age} Jahre!')
        
#Aufgabe 3
class Product():
    
    def __init__(self, name, prod_id, category, price):
        self.name = name
        self.prod_id = prod_id
        self.price = price
        
        if category in ["food", "drinks", "others"]:
            self.category = category
        else:
            self.category = "others"
            
    def apply_discount(self, discount):
        if 0 <= discount <= 100:
            self.price = self.price - self.price * (discount/100)
        else:
            print("Es wurde ein falscher discount eingegeben, deshalb wird ein Standarddiscount von 5% berechnet.")
            self.price = self.price - self.price * 0.05