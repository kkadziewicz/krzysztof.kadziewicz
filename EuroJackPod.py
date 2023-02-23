import random

# Wybierz ilość liczb i dodatkowych liczb, które mają być wylosowane
liczby = 5
dodatkowe_liczby = 2

# Wygeneruj listę liczb do wylosowania
numery = list(range(1,51))
dodatkowe_numery = list(range(1,11))

# Losuj liczby i dodatkowe liczby
wylosowane_liczby = random.sample(numery, liczby)
wylosowane_dodatkowe_liczby = random.sample(dodatkowe_numery, dodatkowe_liczby)

# Sortuj wylosowane liczby i wyświetl wynik
wylosowane_liczby.sort()
wylosowane_dodatkowe_liczby.sort()

print("Wylosowane liczby: ", end="")
for liczba in wylosowane_liczby:
    print(str(liczba) + " ", end="")
print("+ ", end="")
for liczba in wylosowane_dodatkowe_liczby:
    print(str(liczba) + " ", end="")
