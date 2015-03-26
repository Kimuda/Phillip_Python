
#Qn8--Write a program that reads a name and an age for a person, until the name is blank. Once all names have been present the user with an option to list the entered people in alphabetical order, or in descending age order. For either choice, list each person's name followed by their age on a single line. Make sure you output the correct age for the correct person.

names=()
ages=()

name=input("Enter a name: ")

while name != '':
    names=names+(name,)
    age=int(input("enter age for "+name+": "))
    ages=ages+(age,)
    name=input("Enter a name: ")

print("list of names- ",names)
print("list of ages- ",ages)

tuplelist=()
tuplelistordered=()

for i in range(len(names)):
    tuplelist=tuplelist+((names[i],ages[i]),)
    tuplelistordered=sorted(tuplelist, key=lambda tup:tup[0])
    

query=input("enter 'A' to sort the list by name in alphabetical order or 'N' to sort by lowest age: ") 

if query=='A':

    for j in range(len(tuplelistordered)):
        print(tuplelistordered[j][0]+" =>",tuplelistordered[j][1])

#if query=='N'
    
#print("list of tuples of paired names and ages-",tuplelist)
#print(tuplelistordered)


