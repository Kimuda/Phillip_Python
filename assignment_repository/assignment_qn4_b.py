number=int(input("enter number of terms "))
factorial=1
term=0

for i in range(1,number+1):
    factorial=factorial*i

print(number,"!","=",factorial)
