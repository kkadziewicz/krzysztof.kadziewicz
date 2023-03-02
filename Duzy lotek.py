# Importujemy modu� random do losowania liczb
import random

# Definiujemy funkcj�, kt�ra generuje sze�� liczb od 1 do 49
def lotto():
    # Tworzymy pust� list� na wylosowane liczby
    liczby = []
    # Powtarzamy sze�� razy
    for i in range(6):
        # Losujemy liczb� od 1 do 49
        liczba = random.randint(1, 49)
        # Sprawdzamy, czy liczba nie jest ju� na li�cie
        while liczba in liczby:
            # Je�li tak, to losujemy inn� liczb�
            liczba = random.randint(1, 49)
        # Dodajemy liczb� do listy
        liczby.append(liczba)
    # Zwracamy list� wylosowanych liczb
    return liczby

# Wywo�ujemy funkcj� i wy�wietlamy wynik
print(lotto())