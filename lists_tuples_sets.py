list1 = [1, 2, 3, 4, 4]
tuple1 = (1, 2, 3, 4, 4)
set1 = {1, 2, 3, 4, 4}
print(list1)
print(tuple1)
print(set1)

##################################################################

friends = {"Pepe", "Manolo", "Luis"}
abroad = {"Pepe", "Luis"}
local_friends = abroad.symmetric_difference(friends)
print(local_friends)

##################################################################

local_friends = abroad.intersection(friends)
print(local_friends)

##################################################################

numbers = [1, 2, 3]
doubled = [num * 2 for num in numbers]  # doubled = [num for num in numbers]

print(numbers)
print(doubled)

##################################################################

friends = ["Manolo", "Benito"]
start_m = [friend for friend in friends if friend.startswith("M")]

print(friends)
print(start_m)
