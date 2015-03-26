#Qn1-Write a program that reads in names until a blank line is encountered, after which it prints out an English style list, i.e. a comma separated list, where the last name is preceded by the word 'and' instead of a comma.


namelist=[]
name=input("enter name ")

while name!="":
    namelist+=[name]
    name=input("enter name ")

#lastname=input("enter last name ") #not necessary!!
#for i in range(len(namelist)): #not necessary!
#    print(namelist[i]+", ",end="") #not necessary!
    
#print('and {0}'.format(lastname))

print(namelist)

print (", ".join(namelist[:-1]),end="")
   
print(" and",namelist[-1])



