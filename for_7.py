a=int(input("enter first number "))
b=int(input("enter second number "))
total=0

if a>b:
   smaller=b
   bigger=a
else:
   smaller=a
   bigger=b

for i in range(smaller,bigger+1):
   total=total+i

print(total)
