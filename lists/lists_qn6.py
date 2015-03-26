#Write a program that asks the user for their name, and a number, then prints out the user's name a number of times equal to the number they entered.

number=int(input("Enter a number between 1 and 12 "))
monthslist=['January','February','March','April','May','June','July','August','September','October','November','December']

if number<=12:
    print(monthslist[number-1])
else:
    print("number out of range")    


