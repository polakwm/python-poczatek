products= {
    "Jabłko": {"quantity": 10, "unit_price": 4.90},
    "Gruszka": {"quantity": 6, "unit_price": 7.90},
    "Pomarańcza": {"quantity": 6, "unit_price": 5.90},
    "Banan": {"quantity": 6, "unit_price": 6.90}
}
# Poniżej są moje próby
# for name, data in products.items():
#   print(name, "Stan:", data["quantity"], "Cena jedn:", data["unit_price"])
# prnt(products["Jabłko"]["unit_price"],products["Jabłko"]["quantity"])

#Próba 2
# if "Jabłka" in products:
#     print("Klucz istnieje")
# else:
#     print("Nie ma klucza")

#Próba 3, w funkcji print używa się zmienną a nie nazwę listy
# osoby = [
#     {"imie": "Wojciech", "wiek": 30},
#     {"imie": "Anna", "wiek": 25},
#     {"imie": "Piotr", "wiek": 40}
# ]
# for osoba in osoby:
#     print(osoba["imie"], osoba["wiek"])