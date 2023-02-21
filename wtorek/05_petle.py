# petla interakcyjna + literki
# od a do z

# wersja 1 - litery
alfabet = 'abcdefghijklmnoprstuvwxyz'

#for letter in alfabet:
    # print(f"Letter is {letter}")
    # print(letter, end=" / ")

for position, letter in enumerate(alfabet):
    print(f"Letter is {letter},{position}")
    if position == 7:
        print("Siódemka!!!")
