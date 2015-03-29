newlist=[['O95813', 'CER1 DAND4', '', '267'], ['Q8N907', 'DAND5 CER2 CKTSF1B3 GREM3 SP1', '', '189'], ['O60565', 'GREM1 CKTSF1B1 DAND2 DRM PIG2', '', '184'], ['P41271', 'NBL1 DAN DAND1', '4X1J;', '181'], ['Q96S42', 'NODAL', '4N1D;', '347'], ['Q15465', 'SHH', '3HO5;3M1N;3MXW;', '462']]

d1=[]

list3=[]
for i in range(len(newlist)):
    newlist2={}
    #print(i, newlist[i])
    newlist2["Entry"]=newlist[i][0]
    newlist2["Gene_name"]=newlist[i][1]
    newlist2["Cross_ref_pdb"]=newlist[i][2]
    newlist2["Length"]=newlist[i][3]
    list3+=[newlist2]

print(list3)

#[{'Gene_name': 'CER1 DAND4', 'Length': '267', 'Entry': 'O95813', 'Cross_ref_pdb': ''}, 
#{'Gene_name': 'DAND5 CER2 CKTSF1B3 GREM3 SP1', 'Length': '189', 'Entry': 'Q8N907', 'Cross_ref_pdb': ''}, 
#{'Gene_name': 'GREM1 CKTSF1B1 DAND2 DRM PIG2', 'Length': '184', 'Entry': 'O60565', 'Cross_ref_pdb': ''}, 
#{'Gene_name': 'NBL1 DAN DAND1', 'Length': '181', 'Entry': 'P41271', 'Cross_ref_pdb': '4X1J;'}, 
#{'Gene_name': 'NODAL', 'Length': '347', 'Entry': 'Q96S42', 'Cross_ref_pdb': '4N1D;'}, 
#{'Gene_name': 'SHH', 'Length': '462', 'Entry': 'Q15465', 'Cross_ref_pdb': '3HO5;3M1N;3MXW;'}]


