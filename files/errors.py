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

def mean(list_num):
    s=0
    for element in list_num:
        s+=element
    if s==0:
        raise ValueError("looks like you didn't enter any values")
    else:
        return s/len(list_num) #can throw an error, 'division by zero'


listofnumbers=askNumbers() #calling list function 
m=mean(listofnumbers) #calling mean function 
print("The mean of the list ", listofnumbers, "is",m)


        

