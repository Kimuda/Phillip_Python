number=int(input("enter number of terms "))
factorial=1
terms=0

for i in range(1,number+1):
    factorial=factorial*i

    for j in range(i):
        terms=terms+(1.0/factorial)


print("Terms entered return value of ", terms)
