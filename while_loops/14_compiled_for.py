phrase1=input("enter a phrase ")
phrase2=input("enter a phrase ")
letter=input("enter a letter ")
counter1=0
counter2=0


for i in phrase1:
   if i == letter:
       counter1=counter1+1
#print(counter1)

for j in phrase2:
   if j == letter:
       counter2=counter2+1
#print(counter2)

if counter1>counter2:
   print("letter",letter, "occured most in the phrase--", phrase1)
else:
   print("letter", letter, "occured most in the phrase--", phrase2)
