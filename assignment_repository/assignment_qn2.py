alphabet="abcdefghijklmnopqrstuvwxyz"
letterCount=0
phrase=(input("enter a phrase")).lower()
    
if len(phrase) < 26: #eliminate entries less than the length of the alphabet
   print("Phrase not long enough")
   
else:
   for i in range(len(alphabet)):  
       if alphabet[i] in phrase: 
           letterCount = letterCount + 1
   
   if letterCount == 26:
       print("This is a pangram")
   else:
       print("This is not a pangram")
