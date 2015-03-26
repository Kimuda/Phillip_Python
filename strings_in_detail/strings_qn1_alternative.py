#Qn1-Write a program that reads in names until a blank line is encountered, after which it prints out an English style list, i.e. a comma separated list, where the last name is preceded by the word 'and' instead of a comma.


namelist=[]
name=input("enter name ")

while name!="":
    namelist+=[name]
    name=input("enter name ")

lastname=input("enter last name ")
namelist+=['and',lastname]

print(namelist)
 
for i in range(len(namelist)):

    print(namelist[i]+",",end="")

print()

