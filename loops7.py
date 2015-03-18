a=int(input("enter first number"))
b=int(input("enter second number"))
total=0

if a>b:
    counter=b
    top=a
else:
    counter=a
    top=b

while counter<=top:
    total=total+counter
    counter=counter+1
print(total)

       
