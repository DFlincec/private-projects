import json

with open("tickets.json", "r") as file:
    tickets = json.load(file)

print ("Hezlich wilkommen bei ihrer Bahn, Sie haben die folgenden Tickets zur Auswahl:")
#for n in range(len(tickets["tickets"])):
    #print(n, tickets["tickets"][n]["name"])
for n,ticket in enumerate(tickets["tickets"]):
    print(n,ticket["name"])

i = int(input("Bitte geben Sie die entsprechende Zahl für die gewünchte Karte ein:"))
if i < 0 or i >= len(tickets["tickets"]):
    print("Sie haben eine ungültige Auswahl gemacht.")
    exit()
    
print(f"Sie haben das Ticket {tickets['tickets'][i]['name']} ausgewahlt. Der Preis beträgt: {tickets['tickets'][i]['price']} €")

print(f"Der Automat akzeptiert folgende Münzen/Geldscheine: {str(tickets['accepted_cash'])[1:-1]} €")

money_paid = 0

while money_paid < tickets['tickets'][i]['price']:
    paid=tickets['tickets'][i]['price'] - money_paid
    print("Es fehlen noch",paid,"€. Bitte werfen Sie mehr Geld ein.")
    ipaid=int(input())
    if ipaid in tickets["accepted_cash"]:
        money_paid = money_paid + ipaid
    else:
        print(f"Diese Münze/Geld wird leider nicht akzeprtiert, bitte werfen Sie {tickets['accepted_cash']} € ein.")

print(f"Dankeschön für ihren Einkauf. Ihr Rückgeld beträgt {money_paid - tickets['tickets'][i]['price']} €.")