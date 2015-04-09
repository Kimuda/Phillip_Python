def standard_deviation():

    def askNumbers():
        numbers=[]
        tmp=input("give me a number: ").strip()
        while tmp!="":
        
            if tmp.isdigit(): #only numbers are accepted
                tmp=float(tmp)
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
            raise ValueError ("Howdy partner, seems you didn't enter a number, wanna try again?")    
        else: 
            return s/len(list_num)

    def mean_differences(listofnumbers):
        list_of_mean_differences=[]
        for element in listofnumbers:
            list_of_mean_differences+=[m-element]
        return list_of_mean_differences

    def squares(list_of_mean_differences):
        square_of_differences=[]
        for element in list_of_mean_differences:
            square_of_differences+=[element*element]
        return square_of_differences


    listofnumbers=askNumbers() #calling list function 
    m=mean(listofnumbers) #calling mean function
    dm=mean_differences(listofnumbers) #list of mean-item
    msd=squares(dm) #gives a list of the squared differencs
    mean_of_msd_list=mean(msd) #re-using the mean function
    standard_deviation=mean_of_msd_list**(1/2.0) #gives the square root of the mean of the square of differences.

    
    return standard_deviation
    

#print("The mean of the list ", listofnumbers, "is",m,"The standard deviation of the list is ",standard_deviation)
print(standard_deviation)
standard_deviation()


