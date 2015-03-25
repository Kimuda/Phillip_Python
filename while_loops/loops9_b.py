number=input("enter number") #first number before loop
othernumber=0
while number!="": #while data entered is not a space 
           
    number=int(number)
    othernumber=number 
    if number<othernumber:
        print(number) 
    number=input("enter number")
