#Question 4

import sys
import os
import os.path
import textwrap
from sys import argv

filename=argv[1]

##-----Verifying that the path of the file exists and is not a directory

if os.path.exists(filename)==True:
	print("file path entered specifies a file that exists, proceed")
else:
    raise ValueError("Warning the filepath specified does not exist or is a directory")
	

##------Parsing the file, extracting the reads and their positions

def read_seq_parser(filename):
    f=open(filename,"r")
    lines = f.readlines()
    f.close()
    dict2={}
    for i in lines:
        dict2["".join(i).split()[0]]="".join(i).split()[1]
    return dict2
    
#print(read_seq_parser(filename))

##-------Displaying the reads in a vertical viewer


list3=list(read_seq_parser(filename).keys())
#print(list3)
counter=0
x=""
for i in list3:
    counter+=1
           
    #print("{0} {1} {2}".format(counter,'*'*len(range(0,int(i))),read_seq_parser(filename)[i]))
    print("{0} {1} {2}".format(counter,' '*len(range(0,int(i))),read_seq_parser(filename)[i]))
    
   


##-----creating consensus sequence







##----writing fasta file of consensus sequence
    
    
fasta_query=input("Enter name of fasta file, (.fasta or .fa), and directory where you want it created (Empty space for Summary): ")
        while fasta_query!="":
            if os.path.exists(fasta_query)==True:
                print('****WARNING file directory already exists***')
            else:
                system_warning=input("press Enter if you wish to proceed and create the fasta file: ")
                if system_warning=="":
                    fasta_file=open(fasta_query,'a')
                    fasta_file.writelines("> consensus_sequence ID")
                    fasta_file.writelines(consensus_sequence)
                    fasta_file.close()
            fasta_query=input("Enter name of fasta file, (.fasta or .fa), and directory where you want it created(Empty space to EXIT): ")

    
    


    
