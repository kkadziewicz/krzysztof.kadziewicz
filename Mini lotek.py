import random

# Tworzenie pustej listy, do której będą dodawane wylosowane liczby
lotto_numbers = []

# Pętla while losująca 5 unikalnych liczb z zakresu od 1 do 42
while len(lotto_numbers) < 5:
    number = random.randint(1, 42)
    if number not in lotto_numbers:
        lotto_numbers.append(number)

# Sortowanie wylosowanych liczb od najmniejszej do największej
lotto_numbers.sort()

# Wyświetlenie wylosowanych liczb
print("Wylosowane liczby to:", lotto_numbers)
