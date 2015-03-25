phrase=input("enter a phrase here")
letter=input("enter a letter here")
phraselength=len(phrase)
counter=0

while phraselength>=0:
   if phrase[phraselength-1]==letter:
       counter=counter+1
   
   phraselength=phraselength-1

print(counter)
