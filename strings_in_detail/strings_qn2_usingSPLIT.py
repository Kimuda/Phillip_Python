
#Qn2Write a program that reads in a line of space separated names, after which it prints out an English style list, i.e. a comma separated

nameswithspaces=input("enter a list of names separated by a space ") #generates a string of names separated by spaces
newlist=[] #empty list to be filled


newlist=nameswithspaces.split() #generates a list where these spaces have been replaced by commas


print(newlist)

print (", ".join(newlist[:-1]),end="") #if u remove join, they are just names concatenated together <<JOIN>>
   
print(" and",newlist[-1])

  
