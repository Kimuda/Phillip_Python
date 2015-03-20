number=int(input("please enter a number "))
counter=1
factorial=1

while counter<=number:
    factorial=factorial*counter
    counter=counter+1

print(number,"!","=",factorial)


