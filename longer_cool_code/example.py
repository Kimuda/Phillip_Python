a=int(input("enter 1st number "))
b=int(input("enter 2nd number "))
total=0

if a>b:
    counter = b
    top = a
else:
    counter = a
    top = b

while counter<=top:
     total=total+counter
     counter=counter+1

print (total)