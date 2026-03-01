import math

# Stała PI
print(f'Pi = {math.pi}')
print('Pi =', math.pi)

# Funkcja sinus
sin_180=math.sin(math.pi)
print(f'Sin 180 = {sin_180}')
print('Sin 180 =', sin_180)
print("Sin 180 =", math.sin(math.pi))

# Niekończoność
print('math.inf', math.inf)

# Zapis z dolnym podkreśleniem jest równoznaczny temu "bez" - tylko czytelność
very_big_number = 100_000_000_000_000
very_big_number_bez_pod = 100000000000000
the_biggest_number = math.inf

# Nieskończoność jest większa niż cokolwiek innego
print('the_biggest_number > very_big_number:', the_biggest_number > very_big_number)
print('the_biggest_number > very_big_number_bez_pod:', the_biggest_number > very_big_number_bez_pod)