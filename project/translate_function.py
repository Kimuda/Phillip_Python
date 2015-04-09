#translate function,single codon at a time

def Codons():
    codons={}
    CODONS = (
        ('ATA','I'), ('ATC','I'), ('ATT','I'), ('ATG','M'),\
        ('ACA','T'), ('ACC','T'), ('ACG','T'), ('ACT','T'),\
        ('AAC','N'), ('AAT','N'), ('AAA','K'), ('AAG','K'),\
        ('AGC','S'), ('AGT','S'), ('AGA','R'), ('AGG','R'),\
        ('CTA','L'), ('CTC','L'), ('CTG','L'), ('CTT','L'),\
        ('CCA','P'), ('CCC','P'), ('CCG','P'), ('CCT','P'),\
        ('CAC','H'), ('CAT','H'), ('CAA','Q'), ('CAG','Q'),\
        ('CGA','R'), ('CGC','R'), ('CGG','R'), ('CGT','R'),\
        ('GTA','V'), ('GTC','V'), ('GTG','V'), ('GTT','V'),\
        ('GCA','A'), ('GCC','A'), ('GCG','A'), ('GCT','A'),\
        ('GAC','D'), ('GAT','D'), ('GAA','E'), ('GAG','E'),\
        ('GGA','G'), ('GGC','G'), ('GGG','G'), ('GGT','G'),\
        ('TCA','S'), ('TCC','S'), ('TCG','S'), ('TCT','S'),\
        ('TTC','F'), ('TTT','F'), ('TTA','L'), ('TTG','L'),\
        ('TAC','Y'), ('TAT','Y'), ('TAA','*'), ('TAG','*'),\
        ('TGC','C'), ('TGT','C'), ('TGA','*'), ('TGG','W'))

    for i in CODONS:
        codons[i[0].lower()]=i[1]
    return codons

#to transale a whole string of nucleotides

def codonToProtein(codedna,codons):
    protein=""
    for i in range(0,len(codedna),3):
        codon=codedna[i:i+3]
        if len(codon) == 3:
            if codons[codon]=="*":
                break
            protein+=codons[codon]  
    return protein


codons=Codons()
seq="gatcctccatatacaacggtatctccacctcaggttatctcaacaacggaaccatttgca"
#protein=codonToProtein(seq,codons)

#print(protein)

for i in range(0,len(seq),3):
    if seq[i:i+3]=="tct":
        start=seq.find("tct")
        print('blergh',start,seq[start:])
        protein+=codonToProtein(seq[start:],codons)
        print(protein)
    #else:
        #print("No ORF found") 














