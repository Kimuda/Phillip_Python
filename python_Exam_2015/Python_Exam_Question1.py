

dict1={'A':313.21,'T':304.2,'C':289.18,'G':329.21}

dna_sequence=input("Enter a DNA sequence: ")
dna_sequence=dna_sequence.upper()

counter=0
counterA=0
counterC=0
counterG=0
counterT=0
for i in range(len(dna_sequence)):
    if dna_sequence[i]=="A":
       counter+=dict1['A']
       counterA+=dict1['A']
    if dna_sequence[i]=="T":
       counter+=dict1['T']
       counterT=dict1['T']
    if dna_sequence[i]=="G":
       counter+=dict1['G']
       counterG=counterG+1
    if dna_sequence[i]=="C":
       counter+=dict1['C']
       counterC+=dict1['C']
       
    #print(dna_sequence[i],dict1[dna_sequence[i]],counter)
    print("{0}   {1} \t {2}".format(dna_sequence[i],dict1[dna_sequence[i]],counter))
 	
print()
print("--------------------") 	
print("Weight Contribution per base: ")
print("A =",counterA)
print("C =",counterC)
print("G =",counterG)
print("T =",counterT)
print()
print("Total weight: ",counter)
