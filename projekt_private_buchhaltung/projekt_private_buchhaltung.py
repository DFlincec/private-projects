#Aufgabe 1
import pandas as pd
budget = pd.read_csv("budget.csv", sep=";")
budget.info()

#Aufgabe 2
einahmen = budget["In"].sum()
ausgaben = budget["Out"].sum()
print(f"Julia und Mario konnten in den letzten Monaten {round(einahmen - ausgaben)}€ sparen.")

#Aufgabe 3
ausgaben_grupiert = pd.DataFrame(budget, columns=["Category", "Out"])
ausgaben_grup = (ausgaben_grupiert.groupby(by="Category").sum())
print(ausgaben_grup)

#Aufgabe 4
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
expenses_per_category = sns.barplot(data=ausgaben_grup, x="Out", y=ausgaben_grup.index)
expenses_per_category.set_title("Ausgaben pro Kategorie")
expenses_per_category.set(xlabel='Höhe der Ausgaben', ylabel='Kategorie')
expenses_per_category.get_figure().savefig("expenses_per_category.png", bbox_inches="tight")
expenses_per_category.figure.clf()

#Aufgabe 5
import datetime as dt
#budget["Date"] = budget["Date"].apply(lambda x: dt.datetime.strptime(x,"%Y-%M-%d"))
budget["Date"] = pd.to_datetime(budget["Date"], format = "%Y-%m-%d")
ausgaben_pro_monat = budget[["Date", "Out"]].groupby(pd.Grouper(key="Date", freq="M")).sum()
print(ausgaben_pro_monat)
apm_sns = sns.barplot(data=ausgaben_pro_monat, x = ausgaben_pro_monat.index.month_name(), y = "Out")
apm_sns.set_title("Ausgaben pro Monat")
apm_sns.set(xlabel='Monat', ylabel='Ausgaben')
apm_sns.get_figure().savefig("expenses_per_month.png", bbox_inches="tight")