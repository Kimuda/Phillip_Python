#qn2.Modify that progam to print the name of the sequence(first line of a fasta file, starting for '>'), then print the total of nucleotides in the sequence and now print the nucleotides but each line should have 50 characters





f=open("wuch_fasta.fa","r")
seq=[]

for line in f:
    
    if line.startswith(">"):
        print(line.rstrip())
        print("--------------------")
    else:
        seq.extend(line.rstrip('\n\t'))          

mystring = "".join(seq)
#print(mystring)
#x=type(mystring)
#y=len(mystring)
print("Total number of nuclotides is: ",len(mystring))

rest=mystring[:]
while len(rest)>60:
    position=rest[0:60]
    print("\t"+rest[0:position])
#print("\t"+rest)

#def printLinesof60(text):
#    rest=text[:]
#    while len(rest)>60:
#       position=rest[0:60].rfind(" ")+1
#       print("\t"+rest[0:position])
#       rest=rest[position:]
#    print("\t"+rest)

 
