phrase1=input("enter a phrase ")
phrase2=input("enter a phrase ")
letter=input("enter a letter ")
phraselength1=len(phrase1)
phraselength2=len(phrase2)
counter1=0
counter2=0


while phraselength1>=0:
   if phrase1[phraselength1-1]==letter:
       counter1=counter1+1   
   phraselength1=phraselength1-1
#print(counter1)

while phraselength2>=0:
   if phrase2[phraselength2-1]==letter:
       counter2=counter2+1   
   phraselength2=phraselength2-1
#print(counter2)

if counter1>counter2:
   print("letter",letter, "occured most in the phrase--", phrase1)
else:
   print("letter",letter, "occured most in the phrase--", phrase2)


