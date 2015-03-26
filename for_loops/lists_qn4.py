monthslist=["January", "February", "March","April", "May","June","July","August","September","October","November","December"]

number=int(input("enter a number from 1 to 12 "))

while number<=12 and number!=0:
    print(monthslist[number-1])
    break
