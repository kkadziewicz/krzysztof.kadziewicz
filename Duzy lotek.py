# Importujemy modu³ random do losowania liczb
import random

# Definiujemy funkcjê, która generuje szeœæ liczb od 1 do 49
def lotto():
    # Tworzymy pust¹ listê na wylosowane liczby
    liczby = []
    # Powtarzamy szeœæ razy
    for i in range(6):
        # Losujemy liczbê od 1 do 49
        liczba = random.randint(1, 49)
        # Sprawdzamy, czy liczba nie jest ju¿ na liœcie
        while liczba in liczby:
            # Jeœli tak, to losujemy inn¹ liczbê
            liczba = random.randint(1, 49)
        # Dodajemy liczbê do listy
        liczby.append(liczba)
    # Zwracamy listê wylosowanych liczb
    return liczby

# Wywo³ujemy funkcjê i wyœwietlamy wynik
print(lotto())