# petla interakcyjna + iterables

imie = "Krzysztof"
wiek = 55
lista_2 = [3.14, 6, 12]
lista = [3, 54, 3, wiek,  5, 8, lista_2,  imie, 9]

for element in lista:
    print(f"Wartość {element} ma typ {type(element)}")
    if isinstance(element, int):
        print(f"Litera to {chr(element)}")
    else:
        print("Sorry")