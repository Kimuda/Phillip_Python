
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
print(list3)
