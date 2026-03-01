from itertools import cycle

from zamowienia import creat_order_or_not

decision="T"
while decision == "T":
    product=input("Podaj co chcesz kupić: ")
    creat_order_or_not(product)
    decision= input("Czy kontynuujesz zakupy?: T/N")

# print("Brawo!")


# # Moje próby
# x="""<ala ma
# kota>"""
# print(x[1:-1]) #zaczynamy od drugiego znaku (1) i kończymy na przedostatnim

# from itertools import cycle
# for x in cycle(["A", "B", "C"]):
#     print(x)
#     # break