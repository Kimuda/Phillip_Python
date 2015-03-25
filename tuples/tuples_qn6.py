#Qn6Write a program that accepts a list of numbers terminated by a blank line, and stores the result in a tuple, a. Repeat the process to form a second user inputted tuple, b, making sure there are the same number of elements in b as in a. Print out the result of the mathematical addition (not concatenation) of the two tuples as a tuple.


number=input("Enter a number or a blank line to finish making list 1: ")
a=()
b=()

while number!="": #this stages our condition, i.e not a space, continue
        
    number=int(number) #this is placed here because of the while comparison, srings not comparable with integers
    t=(number,)
    a=a+t
    number=input("Enter a number: ") #this restarts the loop or falsifies it

for i in range(len(a)): #limits the entries to the len(a)
    b=b+(int(input("Enter a number or a blank line to finish making list 2: ")), )

print("Tuple a- ",a)
print("Tuple b- ",b)


addition = ()

for i in range(len(a)):
    addition=addition+(a[i]+b[i], )

print("Addition of tuple a and b- ",addition)




