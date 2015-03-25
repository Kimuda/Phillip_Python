phrase=input("enter a phrase here")
letter=input("enter a letter here")
#phraselength=len(phrase)
counter=0

for i in phrase:
   if i == letter:
       counter=counter+1
print(counter)
