list3=[{'Gene_name': 'CER1 DAND4', 'Length': '267', 'Entry': 'O95813', 'Cross_ref_pdb': ''}, 
{'Gene_name': 'DAND5 CER2 CKTSF1B3 GREM3 SP1', 'Length': '189', 'Entry': 'Q8N907', 'Cross_ref_pdb': ''}, 
{'Gene_name': 'GREM1 CKTSF1B1 DAND2 DRM PIG2', 'Length': '184', 'Entry': 'O60565', 'Cross_ref_pdb': ''}, 
{'Gene_name': 'NBL1 DAN DAND1', 'Length': '181', 'Entry': 'P41271', 'Cross_ref_pdb': '4X1J;'}, 
{'Gene_name': 'NODAL', 'Length': '347', 'Entry': 'Q96S42', 'Cross_ref_pdb': '4N1D;'}, 
{'Gene_name': 'SHH', 'Length': '462', 'Entry': 'Q15465', 'Cross_ref_pdb': '3HO5;3M1N;3MXW;'}]

#----Question 2. Create a function that receives a gene name and returns the protein ID.

def genesearch():
    query=(input("enter a gene name to retrieve the protein ID or a blank line to exit: ")).upper()
    listofgenes=""
    while query!="":
        for gene in list3:
            listofgenes=gene["Gene_name"]
            if query in listofgenes: 
                print(gene["Entry"])
        query=(input("enter genename: ")).upper()

genesearch()
