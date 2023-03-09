friends = ["Manolo", "Benito"]
print("Benito" in friends)

##################################################################

movies = ["matrix", "deadpool"]
user_movie = input("Enter a movie title: ").lower()

if user_movie in movies:
    print(f"I also watched {user_movie}! It's amazing.")

else:
    print("I haven't watched that yet.")

##################################################################

number = 7
user_input = input("Enter 'y' if you want to play: ")  # .lower()

if user_input in ("y", "Y"):  # if user_input == "y":
    user_number = int(input("Guess our number: "))

    if user_number == number:
        print("Correct!")

    elif number - user_number in (1, -1):  # if abs(number - user_number) == 1:
        print("You were off by one.")

    else:
        print("Wrong number :(")

else:
    print("Bye!")
