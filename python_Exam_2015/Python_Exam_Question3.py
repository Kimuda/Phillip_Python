#question 3


##--------start of function---------------#######
def codon_getter(codedna):
    #codedna=input("Enter a DNA sequence: ")
    codedna=codedna.upper()
    dict2={}

#---capturing every codon
    list2=[]
    for i in range(0,len(codedna),3):
        codon=codedna[i:i+3]
        if len(codon) == 3:
            list2+=[codon]
#print(list2) 

#----codons without repeats
    list3=[]
    for j in list2:    
        if j not in list3:
            list3+=[j]              
#print(list3)   
#-----counting the codons
    counter=0
    for k in list3:
    #print(k)
        counter=0
        for i in range(len(list2)):
        #counter=0
            if k==list2[i]:
                counter+=1
        dict2[k]=counter 
    return dict2
###------------------------end of function----------------#####



###--------start of program---------------------########
    
codedna=input("Enter a DNA sequence: ")   
dic=codon_getter(codedna)

print("CODON", "TIMES")
for i in list(dic.keys()):   
    print(i,"   ",dic[i])
    


 

