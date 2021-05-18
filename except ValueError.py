print("How many days a week do you workout?")
numDays = input()
try:
    if int(numDays) <= 0:
        print("That's a negative number")
    elif int(numDays) >= 4:
        print("That's a lot of days")
    else:
        print("That's not that many days")
except ValueError:
    print("You did not enter a number")