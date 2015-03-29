#----4. Create a function that prints the proteins IDs and the number of reported genes. The list should be sorted by the number of genes.

list3=[{'Gene_name': 'CER1 DAND4', 'Length': '267', 'Entry': 'O95813', 'Cross_ref_pdb': ''}, 
{'Gene_name': 'DAND5 CER2 CKTSF1B3 GREM3 SP1', 'Length': '189', 'Entry': 'Q8N907', 'Cross_ref_pdb': ''}, 
{'Gene_name': 'GREM1 CKTSF1B1 DAND2 DRM PIG2', 'Length': '184', 'Entry': 'O60565', 'Cross_ref_pdb': ''}, 
{'Gene_name': 'NBL1 DAN DAND1', 'Length': '181', 'Entry': 'P41271', 'Cross_ref_pdb': '4X1J;'}, 
{'Gene_name': 'NODAL', 'Length': '347', 'Entry': 'Q96S42', 'Cross_ref_pdb': '4N1D;'}, 
{'Gene_name': 'SHH', 'Length': '462', 'Entry': 'Q15465', 'Cross_ref_pdb': '3HO5;3M1N;3MXW;'}]

def proteinIDsnumberofgenes():
    print("Protein ID  Number of genes")
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
    
        print(item[0],"    ",item[1])
        #print(sortednumberofgeneslist)

proteinIDsnumberofgenes()
