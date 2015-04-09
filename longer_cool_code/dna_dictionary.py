codon_table = {
    'A': ('GCT', 'GCC', 'GCA', 'GCG'),
    'C': ('TGT', 'TGC'),
    'D': ('GAT', 'GAC'),
    'E': ('GAA', 'GAG'),
    'F': ('TTT', 'TTC'),
    'G': ('GGT', 'GGC', 'GGA', 'GGG'),
    'I': ('ATT', 'ATC', 'ATA'),
    'H': ('CAT', 'CAC'),
    'K': ('AAA', 'AAG'),
    'L': ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'),
    'M': ('ATG',),
    'N': ('AAT', 'AAC'),
    'P': ('CCT', 'CCC', 'CCA', 'CCG'),
    'Q': ('CAA', 'CAG'),
    'R': ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
    'S': ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'),
    'T': ('ACT', 'ACC', 'ACA', 'ACG'),
    'V': ('GTT', 'GTC', 'GTA', 'GTG'),
    'W': ('TGG',),
    'Y': ('TAT', 'TAC'),
    '*': ('TAA', 'TAG', 'TGA'),
}

# for aminoacid in codon_table:
#     print (aminoacid,"=>",end=" ")
#     count=0
#     for codon in codon_table[aminoacid]:
#         print(codon,end="")
#         if (count<len(codon_table[aminoacid])-1):
#             print("-",end="")
#         count += 1
#     print()

inverse_codon_table = {}
for aminoacid in codon_table:
    for codon in codon_table[aminoacid]:
        inverse_codon_table[codon] = aminoacid

dna = "tacgtcaTgtcgaTTTtagcttttTTTTacgtcagtacgtcagtcagtgactgctagttttcgatgcatgctaggctag"
dna = dna.upper()

protein = ""
for i in range(0,len(dna),3):
    codon = dna[i:i+3]
    if len(codon) == 3:
        if inverse_codon_table[codon]=="*":
            break
        protein += inverse_codon_table[codon]


print(protein)















