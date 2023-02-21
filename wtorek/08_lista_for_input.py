colors = ["red", "green"]

ile = int(input("Ile kolorów chcesz podać: "))
for new in range(ile):
    new_color = input("jaki chcesz kolor? ")
    colors.append(new_color)

for color in colors:
    print(f"{color=}")