#Aufgabe 1
list1 = 10, 21, 45, 66, 78
list2 = 10, 22, 46, 66, 78, 90
print(set(list1) ^ set(list2))

#Aufgabe 2
print(set(list1) & set(list2))

#Aufgabe 3
marrios={
    "name" : "Marrios",
    "age" : 1999,
    "payment_options" : ["card", "cash", "online"],
    "available_rooms" : [800, 801, 802, 805, 900, 1000, 1001],
    "price_per_night" : 50,
    "employees": ["carlo", "maria", "marta", "luis", "fernando"]
}

hilten={
    "name" : "Hilten",
    "age" : 1992,
    "payment_options" : ["card", "online"],
    "available_rooms": [100, 800, 801, 805, 1000, 1001],
    "price_per_night" : 70,
    "employees" : ["artur", "maria", "oliver", "xenia"]
}

#Frage 1
nights = 5
cost_marrios = nights * marrios["price_per_night"]
cost_hilten = nights * hilten["price_per_night"]
cost_diff = abs(cost_marrios - cost_hilten)
print (f'Fünf Übernachtungen kosten {cost_marrios}€ im Hotel Marrios und {cost_hilten}€ im Hotel Hilten. Der Preisunterschied sind {cost_diff}€.')

#Frage 2
same_rooms=set(marrios["available_rooms"]) & set(hilten["available_rooms"])
print(f"Guten Tag, könnten Sie mir bitte eines der folgenden Zimmer reservieren:{str(same_rooms)[1:-1]} ? Danke.")

#Frage 3
payment_option_m = marrios["payment_options"]
payment_option_h = hilten["payment_options"]
payment_option_diff = set(payment_option_h) ^ set(payment_option_m)
print(f"Im Hotel Marrios gitb es {len(payment_option_m)} und im Hotel Hilten gibt es {len(payment_option_h)} Zahlungsmöglichkeiten.")
print(f"Die Hotels unterscheiden sich in den folgenden Zahlungsmöglichkeiten:{str(payment_option_diff)[1:-1]}")
#Wie kann ich cash ohne '' printen?

#Frage 4
if 'fernando' in marrios["employees"]:
    print ("Fernando arbeitet in Hotel Marrios, deshalb übernachte ich hier.")
    
if 'fernando' in hilten["employees"]:
    print ("Fernando arbeitet in Hotel Hilten, deshalb übernachte ich hier.")
