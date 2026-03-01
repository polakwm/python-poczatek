import calculations.inwestycja
def odpytaj(tekst):
    wartosc = float(input(tekst))
    return wartosc
print("Kalkulator wartości lokaty z roczną kapitalizacją")

k= odpytaj("Podaj wpłacony kapitał: ")
op=odpytaj("Podaj oprocentowanie: ")
ti=odpytaj("Podaj okres lokaty: ")

suma=calculations.inwestycja.obl_kapital(k,op,ti)
print(f"Po upływie {ti} lat na koncie będziesz miał: {suma:.2f}")
print(f"Po upływie {ti} lat na koncie będziesz miał: {round(suma,2)}")