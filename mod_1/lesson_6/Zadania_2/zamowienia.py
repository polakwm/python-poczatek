# def new_orer(product, ilosc):
from magazyn import products
from mod_1.lesson_6.Zadania_2 import magazyn

orders=[] #lista zamówień tworzona na starcie programu

# def create_order_item(products, name, quantity):
#     if name not in products:
#         raise ValueError("Nie znaleziono produktu")
#     product = products[name]
#     if product["quantity"] < quantity:
#         raise ValueError("Za mało produktu na stanie")
#         total_price = quantity * product["unit_price"]
#         return { "product_name": name, "quantity": quantity, "total_price": total_price }

def creat_order_or_not(product):
    if product not in products:
        print("Nie znaleziono produktu")
    else:
        try:
            ilosc=float(input("Podaj ilość produktu: "))
            print("Stan magazynu przed zamówieniem:",products[product]["quantity"])
            if ilosc <= 0:
                print("Ilość musi być większa od zera.")
            elif ilosc <= products[product]["quantity"]:
                koszt=ilosc*products[product]["unit_price"]
                print(f"Zamówienie przyjęte. Zamówiono {ilosc}, Koszt: {koszt:.2f} zł")
                #Aktualizacja magazynu
                products[product]["quantity"]-=ilosc
                #Dodanie zamówienia do listy
                orders.append({
                "towar": product,
                "quantity": ilosc,
                "unit_price": products[product]["unit_price"],
                "value": koszt
                })
                print("Aktualny stan magazynu:", products[product]["quantity"])
                print("Lista zamówień:")
                print("+--------- -+--------+----------+-----------+")
                print("| Towar     | Ilość  | Cena jedn| Wartość   |")
                print("+--------- -+--------+----------+-----------+")
                for o in orders:
                    print(
                        f"|{o['towar']:<10} | "
                        f"{o['quantity']:<6.1f} | "
                        f"{o['unit_price']:<8.2f} | "
                        f"{o['value']:<9.2f} | "
                    )

            else:
                print(f"Brak wystarczającej ilości towaru. Dostepne: {products[product]["quantity"]}")
        except ValueError:
            print("Ilość musi być liczbą.")
