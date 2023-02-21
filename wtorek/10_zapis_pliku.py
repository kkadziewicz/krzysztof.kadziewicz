klasa = [
    ("Krzysztof Kadziewicz", 1968),
    ("Adam Jurkiewicz", 1974),
    ("Slawomir Wiciak", 1978),
    ("Alicja Kozlowska", 1988),
]

for person in klasa:
    print(f"{person}")

for person_2, year in klasa:
    print(f"{person_2}")

# zapis do pliku

with open("pliczk.txt", "w") as plik:
    for person in klasa:
        plik.write(str(person) + chr(10))