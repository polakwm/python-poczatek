import obliczenia_zad_1_m
# #Zad.1 Oblicz prędkość v
# s = float(input("Podaj dystans w km: "))
# t=float(input("Podaj potrzebny czas w godzinach: "))
# v = obliczenia_zad_1_m.obl_v(s,t)
# print("Wyliczona prędkość =", v)
#
# # Zad.2 Oblicz przeciwprostokątna c
# a=float(input("Podaj wartość przyprostokątnej: a "))
# b=float(input("Podaj wartość przyprostokątnej: b "))
# c= obliczenia_zad_1_m.obl_c(a,b)
# print("Przeciwprostokątna c ma wartość", c)

# Zad.3 Kalkulator obliczający wartość lokaty
k=float(input("Podaj jaką kwotę chcesz wpłacić: "))
op=float(input("Podaj jakie jest oprocentowanie: "))
ti=float(input("Podaj czas lokaty w latach: "))
suma= obliczenia_zad_1_m.obl_kapital(k, op, ti)
print(f"Po upływie {ti} lat na koncie będziesz miał: {suma:.2f}")
print(f"Po upływie {ti} lat na koncie będziesz miał: {round(suma,2)}")
