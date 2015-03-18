counter=0
sequence=input("enter nucleotide sequence ")
while counter<len(sequence):
    if sequence[counter]=='A' or sequence[counter]=='a':
       print('a',end="")
    elif sequence[counter]=='G' or sequence[counter]=='g':
       print('g',end="")
    elif sequence[counter]=='C' or sequence[counter]=='c':
        print('c',end="")
    elif sequence[counter]=='T' or sequence[counter]=='t':
        print('t',end="")
    counter=counter + 1 
print()
