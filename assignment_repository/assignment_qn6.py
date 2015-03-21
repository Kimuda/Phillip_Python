dna=input("enter nucleotide sequence ")
dnalower=dna.lower()
nucleotidesonly=""

#creating upper case copy of dnalower, where no non-(gcta) characters are copied. 

i=0
for i in range(len(dnalower)):
    if dnalower[i]=="a":
       nucleotidesonly = nucleotidesonly+'A'
    elif dnalower[i]=="c":
       nucleotidesonly = nucleotidesonly+'C'
    elif dnalower[i]=="g":
       nucleotidesonly = nucleotidesonly+'G'
    elif dnalower[i]=="t":
       nucleotidesonly=nucleotidesonly+'T'

#nucleotidesonly is an upper case copy containing only nucleotides, while dnalower though in lower case has all the characters, nucleotide and non-nucleotide.
    
print("The number of non-nucleotide sequences is ", len(dnalower)-len(nucleotidesonly))
