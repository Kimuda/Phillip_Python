number=input("enter number ") #first number before loop
counter=0
total=0

while number!="": #while data entered is not a space 
    number=int(number)
    counter=counter+1
    total=total+number #total cummulatively stores numbers

    if number=="": #once entry is space 'break'
       break
    number=input("enter number ") #restart loop

    cont=input('enter yes to continue ')                            
    if cont=='yes':             
       #continue                
       number=input("enter number ")#restart loop?
    else:
       break

average=total/counter #calculation of average

print(average)  #print the average   

                            
