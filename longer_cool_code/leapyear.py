year =  input ("enter a four digit year")

year = int(year)

if not (year % 4==0):
    print (year, "is a NOT a LEAF YEAR")
else:
    if not (year % 100==0):
        print (year, "is a LEAF YEAR")
    else:
        if not (year % 400==0):
            print (year, "is a NOT a LEAF YEAR")
        else:
            print (year, "is a LEAF YEAR")