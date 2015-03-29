list3=[{'Gene_name': 'CER1 DAND4', 'Length': '267', 'Entry': 'O95813', 'Cross_ref_pdb': ''}, 
{'Gene_name': 'DAND5 CER2 CKTSF1B3 GREM3 SP1', 'Length': '189', 'Entry': 'Q8N907', 'Cross_ref_pdb': ''}, 
{'Gene_name': 'GREM1 CKTSF1B1 DAND2 DRM PIG2', 'Length': '184', 'Entry': 'O60565', 'Cross_ref_pdb': ''}, 
{'Gene_name': 'NBL1 DAN DAND1', 'Length': '181', 'Entry': 'P41271', 'Cross_ref_pdb': '4X1J;'}, 
{'Gene_name': 'NODAL', 'Length': '347', 'Entry': 'Q96S42', 'Cross_ref_pdb': '4N1D;'}, 
{'Gene_name': 'SHH', 'Length': '462', 'Entry': 'Q15465', 'Cross_ref_pdb': '3HO5;3M1N;3MXW;'}]

#----3. Create a function that receives protein ID and returns the PDB IDs. If the protein doesn’t have PDBs reported, the function should return False.---


def pdbqueryusingproteinID():
    query=(input("enter a protein ID to retrieve the protein PDB IDs or a blank to exit: ")).upper()
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

        query=(input("enter a protein ID: ")).upper()

pdbqueryusingproteinID()
