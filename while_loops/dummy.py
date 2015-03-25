prompt=input("enter Y to continue")

while prompt=="Y": #Y-loop
    
    number=input("enter number ") #start average loop
    counter=0
    total=0

    while number!="":
        number=int(number)
        counter=counter+1
        total=total+number
        number=input("enter number ") #reload average loop
    #prompt=input("enter Y to continue")

    average=total/counter
    print("The average is ",average)

    prompt=input("enter Y to continue") #Y-loop 

   
