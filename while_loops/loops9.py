number=input("enter number") #user first number before loop
othernumber=1000000000000000000

while number!="": #while data entered is not a space 
    number=int(number)
     
    if number<othernumber: #initial value of othernumber is big
       othernumber=number  #now we are capturing the value of number
   
    number=input("enter number") #restart loop

print(othernumber) #outside the loop, we print the captured value
