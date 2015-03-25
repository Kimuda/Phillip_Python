number=input("enter number")
#prompt=input("enter Y to continue")

while prompt=='Y':

    number=input("enter number ") #first number before loop
    counter=0
    total=0
    
    while number!="": #while data entered is not a space 
        number=int(number)
        counter=counter+1
        total=total+number #total cummulatively stores numbers
        number=input("enter number ") #restart loop
     
  
average=total/counter

print("The average= ", average)
   
                                                          
