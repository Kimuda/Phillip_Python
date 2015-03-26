dna="gacccTTaccggAAAttgcgctTTTAAccctttt"
copydna=""

#creating upper case copy of DNA
i=0
for i in range(len(dna)):
    if dna[i]=="a":
       copydna = copydna+'A'
    elif dna[i]=="c":
       copydna = copydna+'C'
    elif dna[i]=="g":
       copydna = copydna+'G'
    elif dna[i]=="t":
       copydna=copydna+'T'
    else:
       copydna=copydna+dna[i]

#reverse using negative indexes
reverse=""
for i in range(1,len(dna)+1):
    reverse= reverse + copydna[-i]
    #reverse2=copydna[i] +reverse2 --same output--

#RNA replacing all T is reverse to U

rna=""
for i in range(len(reverse)):
    if reverse[i]=="T":
       rna=rna+"U" #capture the u's in position of t's
    else:    #for anything that is not a U, dont change it but add it to rna
       rna=rna+reverse[i]    

#counting g in the sequence
countG=0
countA=0
countC=0
countU=0
for i in range(len(rna)):
    if rna[i]=="G":
       countG=countG+1
    if rna[i]=="A":
       countA=countA+1
    if rna[i]=="C":
       countC=countC+1
    if rna[i]=="U":
       countU=countU+1

GC_ratio=(countG+countC)/len(rna)

print(dna)
print(dna.upper())
print(copydna)
print(reverse)
#print(copydna[::-1]
print(rna)
print("The G count is ", countG,"\nThe A count is ", countA,"\nThe C count is ", countC,"\nThe U count is ", countU)
print("The lenghth of my rna sequence is", len(rna))
print("The GC ratio is ",GC_ratio)
print("total of g+c+a+u= ",countC+countA+countG+countU)
