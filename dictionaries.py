friend_ages = {"Manolo": 25,
               "Benito": 30
               }

print(friend_ages["Manolo"])

friend_ages["Manolo"] = 20
print(friend_ages["Manolo"])

print(friend_ages)

##################################################################

friends = [
    {"name": "Manolo", "age": 25},
    {"name": "Benito", "age": 30}
]

print(friends[0]["name"])

##################################################################

student_attendance = {"Luis": 96,
                      "Pepe": 80,
                      "Ricardo": 100
                      }

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

##################################################################

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

##################################################################

