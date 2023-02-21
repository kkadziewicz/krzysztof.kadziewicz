current_year = 2023
my_birthday = 1968
my_age = current_year - my_birthday
print(f"My age is {my_age}")

if my_age >= 18:
    print("You are adult")
elif my_age < 0:
    print("Not born yet")
else:
    print("You are young")