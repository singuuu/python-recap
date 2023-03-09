add1 = lambda x, y: x + y

print("1", add1(5, 7))

add2 = (lambda x, y: x + y)(5, 7)

print("2", add2)


##################################################################

def double(x):
    return x * 2


sequence = [1, 2, 3, 4]
doubled1 = [double(x) for x in sequence]

print("3", doubled1)

doubled2 = list(map(double, sequence))
print("4", doubled2)

##################################################################

doubled3 = list(map(lambda x: x * 2, sequence))
print("5", doubled3)

##################################################################

users = [
    (0, "Bob", "password"),
    (1, "Manolo", "12345678"),
    (2, "Benito", "fdsawqe432fd"),
    (3, "Shila", "sda321fav"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("User credentials correct!")
else:
    print("User credentials are wrong!")
