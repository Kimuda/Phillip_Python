text=input("please enter palindrome text ")
textlower=text.lower() #this is to avoid Radar not being equal to raDaR
reversetextlower=""

for i in range(1,len(textlower)+1):
    reversetextlower=reversetextlower+textlower[-i]
    
if textlower==reversetextlower:
   print(text, "is a palindrome")
else:
   print(text, "is not a palindrome")
