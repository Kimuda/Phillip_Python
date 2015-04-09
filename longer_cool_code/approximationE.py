
number_of_terms = int(input  ("how many terms? "))

total = 0

for counter in range(number_of_terms+1):
    factorial = 1

    for i in range(1,counter+1):
        factorial = factorial * i

    total = total + 1/factorial #counter

print ("e = ",total)
