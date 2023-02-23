colors = []

while True:
    new_color = input("jaki chcesz kolor? ")

    if new_color.upper() == "KONIEC":
        break

    colors.append(new_color)

for color in colors:
    print(f"{color}")