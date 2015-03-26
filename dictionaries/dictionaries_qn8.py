
#qn8.Write a program that reads in names until a blank line is entered, and prints out each unique name and the number of times it was entered.

dictionary={}
name=input("Enter a name: ")

while name!="":
    
    if name in dictionary: #we are assigning name- values, which is cummulative, 1+number of more times
        dictionary[name]=dictionary[name]+1
    else:
        dictionary[name]=1 

    name=input("Enter a name: ")

print(dictionary)
