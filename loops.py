number = 7

while True:
    user_input = input("Would you like to play? (Y/n): ").lower()

    if user_input == "n":
        print("Bye!")
        break

    elif user_input == "y":
        user_number = int(input("Guess our number: "))

        if user_number == number:
            print("Correct!")
            break

        elif number - user_number in (1, -1):  # if abs(number - user_number) == 1:
            print("You were off by one.")

        else:
            print("Wrong number :(")

    else:
        print("Wrong option.")

##################################################################

friends = ["Manolo", "Benito"]

for friend in friends:
    print(f"{friend} is my friend!")

##################################################################

for number in range(4):
    print(f"{number} is between 0 and 4.")

##################################################################

grades = [35, 64, 78, 12, 83]
total = sum(grades)
amount = len(grades)

print(total / amount)