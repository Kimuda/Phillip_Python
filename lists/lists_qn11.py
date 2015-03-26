#11. Write a program that asks the user for a number from 1 to 12, and then prints out the name of corresponding month, and the number of days in that month, in the form: "January has 31 days."

number=int(input("Enter a number between 1 and 12 "))
monthslist=['January','February','March','April','May','June','July','August','September','October','November','December']
monthdays=[31,28,31,30,31,31,30,31,30,31,30,31]

if number<=12:
    print(monthslist[number-1], "has", monthdays[number-1], "days")
else:
    print("number out of range")
