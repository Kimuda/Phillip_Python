
uniprot_text="""Entry	Gene names	Cross-reference (PDB)	Length
O95813	CER1 DAND4		267
Q8N907	DAND5 CER2 CKTSF1B3 GREM3 SP1		189
O60565	GREM1 CKTSF1B1 DAND2 DRM PIG2		184
P41271	NBL1 DAN DAND1	4X1J;	181
Q96S42	NODAL	4N1D;	347
Q15465	SHH	3HO5;3M1N;3MXW;	462"""

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
for i in range(len(newlist)):
    newlist2={}
    #print(i, newlist[i])
    newlist2["Entry"]=newlist[i][0]
    newlist2["Gene_name"]=newlist[i][1]
    newlist2["Cross_ref_pdb"]=newlist[i][2]
    newlist2["Length"]=newlist[i][3]
    list3+=[newlist2]
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
  
    


