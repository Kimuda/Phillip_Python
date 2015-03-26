
#Qn2Write a program that reads in a line of space separated names, after which it prints out an English style list, i.e. a comma separated

nameswithspaces=input("enter a list of names separated by a space ")

newlist1=[]
newlist2=[]
name=""


for character in nameswithspaces:
    if character!=" ":
        name=name+character
    else:
        newlist2=newlist2+[name]
        name=""

    if name!="":
        newlist1=newlist2+[name]

print(newlist1)

print (", ".join(newlist1[:-1]),end="")
   
print(" and",newlist1[-1])

  
