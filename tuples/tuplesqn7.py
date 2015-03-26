#Qn7.Write a program that reads a name and an age for a person, until the name is blank. As each name age pair is entered, store names in a list, and ages in another. Print a list of tuples of paired names and ages.

#what's new >>> d=[4,5,6],tuple(d),converts a list d into a tuple, d=(4,5,6) -useful cheat when stuck<<< 
#>>>growing the tuple of tuples d=d+((a[i],b[i]),)<<<

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

for i in range(len(names)):
    tuplelist=tuplelist+((names[i],ages[i]),)
    
print("list of tuples of paired names and ages-",tuplelist)

