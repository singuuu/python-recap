day_of_week = input("What day of the week is it today? ").lower()
print(day_of_week == "monday")

##################################################################

if day_of_week == "monday":
    print("Have a great start to your week!")

elif day_of_week == "friday":
    print("Come on! It's Friday!")

else:
    print("Today is not Monday")

##################################################################

if day_of_week != "monday":
    print("Full speed ahead!")

print("This always runs because of indentation")
