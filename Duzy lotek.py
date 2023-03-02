import random

# Tworzenie pustej listy, do której będą dodawane wylosowane liczby
lotto_numbers = []

# Pętla while losująca 6 unikalnych liczb z zakresu od 1 do 49
while len(lotto_numbers) < 6:
    number = random.randint(1, 49)
    if number not in lotto_numbers:
        lotto_numbers.append(number)

# Sortowanie wylosowanych liczb od najmniejszej do największej
lotto_numbers.sort()

# Wyświetlenie wylosowanych liczb
print("Wylosowane liczby to:", lotto_numbers)
