###-------------importing the data----------------------------------------------------###

def readGenbank2(filename):
    f=open("TCP1_beta.gb","r")
    lines = f.readlines()
    f.close()
    return lines

###-------------processing the file, in line chunks------------------------------------#### 

def processLocus(lines):
    return lines

lines=readGenbank2("TCP1_beta.gb")

####-------------translation functions-------------------------------------------------######

#-----translate function,single codon at a time

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

#------to transale a whole string of nucleotides

def codonToProtein(codedna,codons):
    protein=""
    for i in range(0,len(codedna),3):
        codon=codedna[i:i+3]
        if len(codon) == 3:
            if codons[codon]=="*":
                break
            protein+=codons[codon]  
    return protein


#---------------building the dictionary------------------------------------------------#####

list0=[]
list_position=[]
for i in range(len(lines)):
    a_string=lines[i]
    key = a_string[:12]
    if key.startswith(' ')==False and len(key)<=12:
        list0+=[key.strip()]
        list_position+=[i]

genbank ={}
for i in range(len(list0)-1):
    if list0[i]=="LOCUS":
        locus_list = processLocus(lines[list_position[i]:list_position[i+1]])
        
        for i in locus_list:
            x=i.split()[1:]
        genbank["LOCUS"]=x     
 
    elif list0[i]=="DEFINITION":
        definition_list = processLocus(lines[list_position[i]:list_position[i+1]])
        x=[definition_list[0][12:].strip()+definition_list[1][12:].strip()]
        for i in x:
            b=i
        genbank["DEFINITION"]=b
    elif list0[i]=="ACCESSION":
        accession_list=processLocus(lines[list_position[i]:list_position[i+1]])
        genbank["ACCESSION"]=accession_list[0][12:].strip()
    elif list0[i]=="VERSION":
        version_list=processLocus(lines[list_position[i]:list_position[i+1]])
        genbank["VERSION"]=version_list[0][12:].split()
    elif list0[i]=="KEYWORDS":    
        keyword_list=processLocus(lines[list_position[i]:list_position[i+1]])
        genbank["KEYWORDS"]=keyword_list[0][12:].strip()
    elif list0[i]=="SOURCE":
        source_list=processLocus(lines[list_position[i]:list_position[i+1]])
        genbank["SOURCE"]=[source_list[0][12:].strip()]        
        ogarnism_dic={}
        x=source_list[1:]
        for i in x:
            b=i[12:].strip("\n")
            ogarnism_dic["ORGANISM"]=b.split()
        genbank["SOURCE"]+=[ogarnism_dic]
    elif list0[i]=="REFERENCE":
        reference_list=processLocus(lines[list_position[i]:list_position[i+1]])
             
    elif list0[i]=="FEATURES":
        features_list=processLocus(lines[list_position[i]:list_position[i+1]])
        genbank["FEATURES"]=[features_list[0][12:].strip()]

    elif list0[i]=="ORIGIN":
        origin_list=processLocus(lines[list_position[i]:list_position[i+1]])
         
#print(genbank) #stop and check

##--------------importing DNA into dictionary---------------------------------------------####

data=" ".join(origin_list)
origin=data.find('ORIGIN') #where to start frm
start=data.find('1',origin) #move the pointer to the second line that starts with 1
end=data.find('//',origin) #establish a stop point
dna_value=data[start:end].split('\n') #remove the new lines
dna_sequence="" 
                       
for item in dna_value:
    no_spaces=item.split()
    dna_sequence+=''.join(no_spaces[1:]) #remove the first line containing numbers
genbank['ORIGIN']=dna_sequence #adding the contents of origin to the dictionary

#print(genbank['ORIGIN']) #stop and check


##---------------importing Features into dictionary------------------------------------------####

##--------------------------------------------source
SOURCE_dic={}
z=[]
keyword="     source          "
data2=" ".join(features_list)
nsource=data2.count(keyword)
#find the occurences
keylocs=[]
k=0
for i in range(nsource):
    t=data2.find(keyword,k)
    keylocs.append(t)
    k=t+10  
for j in range(len(keylocs)):
    end=data2.find('CDS',keylocs[j])
    z+=[data2[keylocs[j]:end].split()]
SOURCE_dic["source"]=z
genbank["FEATURES"]+=[SOURCE_dic]

#print(genbank["FEATURES"]) #stop and check

##--------------------------------------------CDS
CDS_dic={}
keyword="     CDS             "
data3=" ".join(features_list)
nsource=data3.count(keyword)
#find the occurences
keylocs=[]
k=0
for i in range(nsource):
    t=data3.find(keyword,k)
    keylocs.append(t)
    k=t+10
#print(keylocs)
x=[]
for j in range(len(keylocs)):
    end=data3.find('     gene            ',keylocs[j])
    #print(data3[keylocs[j]:end].split())
    x+=[data3[keylocs[j]:end].split()]
CDS_dic["CDS"]=x
genbank["FEATURES"]+=[CDS_dic]

#print(genbank["FEATURES"]) #stop and check

##---------------------------------------------gene
gene_dic={}
keyword="     gene            "
data4=" ".join(features_list)
nsource=data4.count(keyword)
#find the occurences
keylocs=[]
k=0
for i in range(nsource):
    t=data4.find(keyword,k)
    keylocs.append(t)
    k=t+10
#print(keylocs)
y=[]
for j in range(len(keylocs)):
    end=data4.find('CDS',keylocs[j])
    #print(data3[keylocs[j]:end].split())
    y+=[data4[keylocs[j]:end].split()]
gene_dic["GENE"]=y
genbank["FEATURES"]+=[gene_dic]
#print(genbank["FEATURES"]) #stop and check

##---------------REFERENCES into dictionary------------------------------------------####

data5=" ".join(lines)
origin=data5.find("REFERENCE   ")
start=data5.find("REFERENCE   ",origin)
end=data5.find('FEATURES',origin)
reference_text=data5[start:end]
#print(reference_text)

keyword="REFERENCE   "
data6=reference_text
nsource=data6.count(keyword)
#print(nsource)
keylocs=[]
k=0
for i in range(nsource):
    t=data6.find(keyword,k)
    keylocs.append(t)
    k=t+10
#print(keylocs)
ref_list=[]
for j in range(len(keylocs)-1):
    end=data6.find("REFERENCE   ",keylocs[j+1])
    ref_list+=[data6[keylocs[j]:end].split("\n")]
#print(ref_list)
#print(" ".join(reference_list).split())

genbank["REFERENCE"]=[]
genbank["REFERENCE"]+=ref_list+[" ".join(reference_list).split("\n")]

#print(genbank) #stop and check----------dictionary complete------------------################

##----indexing the references, while building the data structure would have been the easier option, but here is my fix.
author_list=[]
for i in range(len(genbank["REFERENCE"])):
    data7=" ".join(genbank["REFERENCE"][i][1:])
    origin=data7.find("  AUTHORS   ") 
    start=data7.find("  AUTHORS   ",origin)
    end=data7.find("  TITLE     ")
    author_list+=[" ".join(data7[start:end].split())[5:]]
#print(author_list)

title_list=[]
for i in range(len(genbank["REFERENCE"])):
    data7=" ".join(genbank["REFERENCE"][i][1:])
    origin=data7.find("  TITLE     ") 
    start=data7.find("  TITLE     ",origin)
    end=data7.find("  JOURNAL   ")
    title_list+=[" ".join(data7[start:end].split())[6:]]
#print(title_list)

journal_list=[]
for i in range(len(genbank["REFERENCE"])):
    data7=" ".join(genbank["REFERENCE"][i][1:])
    origin=data7.find("  JOURNAL   ") 
    start=data7.find("  JOURNAL   ",origin)
    end=data7.find("FEATURES             ")
    journal_list+=[" ".join(data7[start:end].split())[5:]]
#print(journal_list)
###----------------------references fix-------------------------------######


#print(">gi|{0}|ref|{1}|{2}".format(genbank['VERSION'][1][3:],genbank['ACCESSION'],genbank['DEFINITION']))

#print(genbank['VERSION'][1][3:])
#print(genbank['ACCESSION'])
print(genbank['DEFINITION'])
