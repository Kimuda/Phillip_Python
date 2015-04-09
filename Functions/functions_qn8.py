def askNumbers():
    numbers=[]
    tmp=input("give me a number: ").strip()
    while tmp!="":
        
        if tmp.isdigit(): #only numbers are accepted
            tmp=int(tmp)
            numbers=numbers+[tmp]
        else:
            print("you better enter a number") 

        tmp=input("give me a number: ").strip()
    return numbers

def squares(list_num):
    s=0
    for element in list_num:
        s+=element*element
    return s


listofnumbers=askNumbers() #calling list function 
sum_of_squares=squares(listofnumbers) #calling mean function 
print("The sum of squares of the list ", listofnumbers, "is",sum_of_squares)


        

