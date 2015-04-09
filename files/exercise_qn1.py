#Qn1.Create a program that receives the name of a fasta file(use this file as an example) from the command line, and print the content of the file.

f=open("wuch_fasta.fa","r")

for line in f:
    print(line.rstrip())
