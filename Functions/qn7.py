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
    return s/len(list_num)


listofnumbers=askNumbers() #calling list function 
m=mean(listofnumbers) #calling mean function 
print("The mean of the list ", listofnumbers, "is",m)


        

