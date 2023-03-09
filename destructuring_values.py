x, y = 5, 11
print(x)
print(y)

t = (6, 9)
x, y = t
print(x)
print(y)

##################################################################

people = [
    ("Manolo", 25, "Nyapas1"),
    ("Benito", 30, "Nyapas2"),
]

for name, _, profession in people:
    print(f"Name: {name}, Profession: {profession}")

##################################################################

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
