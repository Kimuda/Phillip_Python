
uniprot_text="""Entry	Gene names	Cross-reference (PDB)	Length
P01009	SERPINA1 AAT PI PRO0684 PRO2209	1ATU;1D5S;1EZX;1HP7;1IZ2;1KCT;1OO8;1OPH;1PSI;1QLP;1QMB;2D26;2QUG;3CWL;3CWM;3DRM;3DRU;3NDD;3NDF;3NE4;3T1P;7API;8API;9API;	418
P08697	SERPINF2 AAP PLI		491
P01023	A2M CPAMD5 FWP007	1BV8;2P9R;4ACQ;	1474
Q16186	ADRM1 GP110	2KQZ;2KR0;2L5V;2MKZ;	407
P01008	SERPINC1 AT3 PRO0309	1ANT;1ATH;1AZX;1BR8;1DZG;1DZH;1E03;1E04;1E05;1JVQ;1LK6;1NQ9;1OYH;1R1L;1SR5;1T1F;1TB6;2ANT;2B4X;2B5T;2BEH;2GD4;2HIJ;2ZNH;3EVJ;3KCG;4EB1;	464
Q6UY14	ADAMTSL4 TSRC1 PP1396 UNQ2803/PRO34012		1074
O75173	ADAMTS4 KIAA0688 UNQ769/PRO1563	2RJP;3B2Z;4WK7;4WKE;4WKI;	837
Q9H3M9	ATXN3L ATX3L MJDL	3O65;	355
P54252	ATXN3 ATX3 MJD MJD1 SCA3	1YZB;2AGA;2DOS;2JRI;2KLZ;	364"""


uniprot_text_list=uniprot_text.split("\n")
protein_list=uniprot_text_list[1:]
#print(uniprot_text_list,protein_list)

d=[]
newlist=[]
for i in protein_list:
    d=i.split("\t")
    newlist+=[d]
#print(newlist)

list3=[]
counter=0
counter2=len(newlist)-1

while counter<len(newlist):
     
    newlist2={}
    
    newlist2["Entry"]=newlist[counter2][0]
    newlist2["Gene_name"]=newlist[counter2][1]
    newlist2["Cross_ref_pdb"]=newlist[counter2][2]
    newlist2["Length"]=newlist[counter2][3]
    list3+=[newlist2]

    counter=counter+1
    counter2=counter2-1
#print(list3)

 

#----Question 1. Create a function that returns the protein ID of the shortest protein----

def ID_of_shortest_protein():
    list_sorted_by_length = sorted(list3, key=lambda k: k['Length'])
    protein_with_shortest_length=list_sorted_by_length[0]
    print("The protein ID of the shortest protein is-",protein_with_shortest_length["Entry"])

ID_of_shortest_protein()



#----Question 2. Create a function that receives a gene name and returns the protein ID.----

def genesearch():
    query=(input("Enter a gene name to retrieve the protein ID or a blank line to exit: ")).upper()
    listofgenes=""
    while query!="":
        for gene in list3:
            listofgenes=gene["Gene_name"]
            if query in listofgenes: 
                print("Protein ID for",query,"is",gene["Entry"])
                      
        query=(input("To exit enter a blank line or Enter a gene name to continue: ")).upper()

genesearch() 
#GLITCHES; even a single letter in query, returns a result, and when no match is found the user is not informed. 


#----Question 3. Create a function that receives protein ID and returns the PDB IDs. If the protein doesn’t have PDBs reported, the function should return False.

def pdbqueryusingproteinID():
    query=(input("Enter a protein ID to retrieve the protein PDB IDs or a blank line to exit: ")).upper()
    listofproteinIDs=""
    while query!="":
        for proteinID in list3:
            listofproteinIDs=proteinID["Entry"]
            if query in listofproteinIDs: 
                if proteinID["Cross_ref_pdb"]!="":
                    commaseperatedpdbs=proteinID["Cross_ref_pdb"].split(";")
                    for i in commaseperatedpdbs:
                        if i!="":
                            print(i+(","),end="")
                    print()      
                else:
                    print("False")

        query=(input("To exit enter a blank line or Enter a protein ID to continue: ")).upper()

pdbqueryusingproteinID() 
#GLITCHES; even a single letter can return a result, and when no match is found the user is not informed.



#----Question 4. Create a function that prints the proteins IDs and the number of reported genes. The list should be sorted by the number of genes.

def proteinIDsnumberofgenes():
    print("Protein ID\tNumber of genes")
    list2=[]
    for item in list3:
       list2=list2 + [[item["Entry"]]+item["Gene_name"].split()]
   
    newdictionary={t[0]:t[1:] for t in list2}

    #print(newdictionary
    numberofgeneslist=[]
    for key in newdictionary:
       numberofgeneslist+=[[key]+[len(newdictionary[key])]]
   
    sortednumberofgeneslist=sorted(numberofgeneslist, key=lambda k: k[1])
       #print(key,len(newdictionary[key]))
    #print(numberofgeneslist)
    for item in sortednumberofgeneslist:
    
        print(item[0],"\t\t",item[1])
        #print(sortednumberofgeneslist)

proteinIDsnumberofgenes()  


#----Question 5. Create a function that prints a list of pairs of all the reported combinations of genes and PDBs 

def gene_names_paired_with_pdbs():
    print("Gene_name\tCross_ref_pdb")
    for item in list3:
        for item2 in item["Cross_ref_pdb"].split(";"):
            if item2!="":
                for item3 in item["Gene_name"].split():
                    print(item3,'\t\t',item2)

gene_names_paired_with_pdbs()
  
    
