###-------------importing the data----------------------------------------------------###
import sys

from sys import argv

script, filename=argv

def readGenbank2(filename):
    f=open(filename,"r")
    lines = f.readlines()
    f.close()
    return lines

###-------------processing the file, in line chunks------------------------------------#### 

def processLocus(lines):
    return lines

lines=readGenbank2(filename)

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


##----------menu--------------####
a="="*60
print()
print('GBK Reader-({})DNA'.format(filename),"\n"+a)
print("Sequence:",genbank["ACCESSION"],"("+genbank["LOCUS"][0]+",",genbank["LOCUS"][1]+genbank["LOCUS"][2]+")")
print("Description: "+genbank["DEFINITION"]) #--I changed Description so that it's more informative,the original as per instructions is below
#print("Description:"+genbank["SOURCE"][0]) #---prints <Description: Saccharomyces cerevisiae (baker's yeast)> same as print statement below 
print("Source: "+genbank["SOURCE"][0])
print("Number of References:",len(genbank["REFERENCE"]))
print("Number of Features:",(len(genbank["FEATURES"][1]["source"])+len(genbank["FEATURES"][2]["CDS"])+len(genbank["FEATURES"][3]["GENE"])),"\n"+a) 
query = input("R:References S:Sequence M:Motif T:Translate F:Features E:Export Q:Quit > ")
##----------menu--------------###

#<<<<<<<<Modules>>>>>>>>>>>>>>>>#

import textwrap #module imported for printing 60 lines at time

import re #module imported for regular expressions 

import os

import os.path

#<<<<<<<<Modules>>>>>>>>>>>>>>>>#


########______________R for Reference_______________################

while query!="":
    if query=="R":
        print()
        print("There are",len(genbank["REFERENCE"]),"articles reported for the sequence",genbank["ACCESSION"])
        for i in range(len(genbank["REFERENCE"])):
            print([i+1],genbank["REFERENCE"][i][1][12:])
        ref_query=input("Input the number of a reference for details (M for the Menu) >")
        while ref_query!="M":
            ref_query=int(ref_query)
            if ref_query<=len(genbank["REFERENCE"]):
                print("Title:","\n\t",title_list[ref_query-1])
                print("Authors:","\n\t",author_list[ref_query-1])
                print("Journal:","\n\t",journal_list[ref_query-1])
            else:
                print("<The Number you have entered exceeds the number of references, please try again>")
            ref_query=input("Input the number of a reference for details (M for the Menu) > ") 

#####__________________S for sequence_________________####################

    if query=="S":
        range_query=input("Enter range in the format e.g [3,2) or (3,2) or (3,2] or [3,2] for print out of nucleotides: ")
        while range_query!="M":
            endx=range_query.find(",")
            #print("x",range_query[1:endx]) #that takes care of x          
            origin=range_query.find(",")
            #print("y",range_query[origin+1:-1]) #that takes care of y
            x=int(range_query[1:endx])  
            y=int(range_query[origin+1:-1])
            #print(x,"-",y) #quick stop and check of the int values of x and y
            if x>len(genbank["ORIGIN"]) or y>len(genbank["ORIGIN"]):
                print("Coordinates entered are outside of the range, please try again")
            elif range_query[0]=="(" and range_query[-1]==")":
                print("\n".join(textwrap.wrap(genbank['ORIGIN'][x:y],60)).upper())
            elif range_query[0]=="[" and range_query[-1]=="]":
                print("\n".join(textwrap.wrap(genbank['ORIGIN'][x-1:y+1],60)).upper())
            elif range_query[0]=="[" and range_query[-1]==")":    
                print("\n".join(textwrap.wrap(genbank['ORIGIN'][x-1:y],60)).upper())
            elif range_query[0]=="(" and range_query[-1]=="]":    
                print("\n".join(textwrap.wrap(genbank['ORIGIN'][x:y+1],60)).upper())        
            range_query=input("Enter range e.g [3,2) or (3,2) or (3,2] or [3,2] for print out of nucleotides (M for the Menu) : ") 

#####__________________M for Motif_____________________________########################


    if query=="M":
        text=input("""Enter a motif to search for in the sequence (the wildcard character '?' represents any nucleotide in that position
and '*' none or many in that position (Blank line to Exit) >""")
        while text!="":
            letter_list=["A","G","C","T","?","*"]
            text=text.upper()
            if len(text)>=5 and all(c in letter_list for c in text):
                replacewith1 = "[AGCT]?" #the regular expression for '?'
                replacewith2= "[AGCT]*"  #the regular expression for '*'
                origin1=text.find("?")
                origin2=text.find("*")                
                list1=list(text)
                if origin1!=-1 and origin2!=-1: #in the event both '?' and '*' are present
                    list1[origin1]=replacewith1
                    list1[origin2]=replacewith2
                    motif="".join(list1)
                elif origin1==-1 and origin2!=-1: #in the event there isn't a '?'
                    list1[origin2]=replacewith2
                    motif="".join(list1)
                elif origin2==-1 and origin1!=-1: #in the event there isn't a '*'
                    list1[origin1]=replacewith1
                    motif="".join(list1)
                elif origin2==-1 and origin1==-1: #in the event there's isn't a '?' or '*' 
                    motif=text             
                #print(motif,origin2,origin1)    
                regexobj=re.compile(motif,re.IGNORECASE)
                print("Searching for the motif",text,"...")
            else:
                print("<<Motif pattern too short or contains non-nucleotide characters, please try again>>")
                break #fix for non-nucleotide characters entered breaking the entire algorithm

            list_all=regexobj.findall(genbank['ORIGIN']) 
            #print(list_all)
            list_iter=regexobj.finditer(genbank['ORIGIN'].upper())
            counter=1
            counter2=len(list_all)
            for s in list_iter:
                #print(s.group())
                #print(s.span())
                #print(s.start())
                #print(s.end())
                print("Match",counter,"of",counter2)
                
                if origin1!=-1 and origin2!=-1: #where both '?' and "*" are present
                    if origin1<origin2:
                        x=text[:origin1]
                        y=text[origin1+1:origin2]
                        z=text[origin2+1:]
                        end=s.group().find(y)
                        end2=s.group().find(z)
                        p=len(y)
                        print("{0}{1}{2}{3}{4}".format(genbank['ORIGIN'][s.start()-5:s.start()],[s.start()],x.lower()+s.group()[origin1:end]+y.lower()+s.group()[end+p:end2]+s.group()[end2:].lower(),[s.end()],genbank['ORIGIN'][s.end():s.end()+5]))
                    else:
                        x=text[:origin2]
                        y=text[origin2+1:origin1]
                        z=text[origin1+1:]
                        end=s.group().find(y)
                        end2=s.group().find(z)
                        p=len(y)
                        print("{0}{1}{2}{3}{4}".format(genbank['ORIGIN'][s.start()-5:s.start()],[s.start()],x.lower()+s.group()[origin1:end]+y.lower()+s.group()[end+p:end2]+s.group()[end2:].lower(),[s.end()],genbank['ORIGIN'][s.end():s.end()+5]))
                elif origin1!=-1 and origin2==-1: #no '*'
                    x=text[:origin1]
                    y=text[origin1]
                    z=text[origin1+1:]
                    end=text.find(y)
                    print("{0}{1}{2}{3}{4}{5}{6}".format(genbank['ORIGIN'][s.start()-5:s.start()],[s.start()],x.lower(),s.group()[end],s.group()[end:].lower(),[s.end()],genbank['ORIGIN'][s.end():s.end()+5]))
                elif origin1==-1 and origin2!=-1: #no '?'
                    x=text[:origin2]
                    y=text[origin2]
                    z=text[origin2+1:]
                    end=text.find(y)    
                    print("{0}{1}{2}{3}{4}{5}{6}".format(genbank['ORIGIN'][s.start()-5:s.start()],[s.start()],x.lower(),s.group()[end],s.group()[end:].lower(),[s.end()],genbank['ORIGIN'][s.end():s.end()+5]))
                elif origin2==-1 and origin1==-1: #neither '*' nor '?' are present
                    print("{0}{1}{2}{3}{4}".format(genbank['ORIGIN'][s.start()-5:s.start()],[s.start()],s.group().lower(),[s.end()],genbank['ORIGIN'][s.end():s.end()+5]))      
                counter+=1        

            text=input("""Enter Motif (Blank line to Exit) >""")



####_____________________T for Translate__________________________________stop codons are TAG,TAA and TGA___################# 


    if query=="T":
        range_query=input("Enter range in the format e.g [3,2) or (3,2) or (3,2] or [3,2] for print out of nucleotides, or FULL for the whole protein translated: ")
        if range_query=="FULL":
            seq=genbank['ORIGIN']
            #print(seq)
            codons=Codons()
            protein=""
            for i in range(0,len(seq),3):
                if seq[i:i+3]=="atg":
                    start=seq.find("atg")
                    protein+=codonToProtein(seq[start:],codons)
            print("\n".join(textwrap.wrap(protein,60)).upper())
        else:
            while range_query!="":
                endx=range_query.find(",")
                origin=range_query.find(",")
                x=int(range_query[1:endx])  
                y=int(range_query[origin+1:-1])
                if x>len(genbank["ORIGIN"]) or y>len(genbank["ORIGIN"]):
                    print("Coordinates entered are outside of the range, please try again")
                elif range_query[0]=="(" and range_query[-1]==")":
                    seq=genbank['ORIGIN'][x:y]
                elif range_query[0]=="[" and range_query[-1]=="]":
                    seq=genbank['ORIGIN'][x-1:y+1]
                elif range_query[0]=="[" and range_query[-1]==")":    
                    seq=genbank['ORIGIN'][x-1:y]
                elif range_query[0]=="(" and range_query[-1]=="]":  
                    seq=genbank['ORIGIN'][x:y+1] 
                #print(seq)

                orf_query=input("Select which ORF to check (1,2,3,or a blank line for all three) :")

                if orf_query=="1": ##-------first ORF
                    seq=seq[0:]
                    codons=Codons()
                    protein=""
                    for i in range(0,len(seq),3):
                        if seq[i:i+3]=="atg":
                            start=seq.find("atg")
                            protein+=codonToProtein(seq[start:],codons)
                    print("ORF:1","\n","\nAmino acids sequence from nucleotide",x,"to",y,"in the 1st ORF","\n"+"\n".join(textwrap.wrap(protein,60)).upper())
                    if protein=="":
                        print('No ORF found, please try again')
    
                elif orf_query=="2": ##-----------second ORF
                    seq=seq[1:]
                    codons=Codons()
                    protein=""
                    for i in range(0,len(seq),3):
                        if seq[i:i+3]=="atg":
                            start=seq.find("atg")
                            protein+=codonToProtein(seq[start:],codons)
                    print("ORF:2","\n","\nAmino acids sequence from nucleotide",x,"to",y,"in the 2nd ORF","\n"+"\n".join(textwrap.wrap(protein,60)).upper())
                    if protein=="":
                        print('No ORF found, please try again')
       
                elif orf_query=="3":  ##--------------third ORF
                    seq=seq[2:]
                    codons=Codons()
                    protein=""
                    for i in range(0,len(seq),3):
                        if seq[i:i+3]=="atg":
                            start=seq.find("atg")
                            protein+=codonToProtein(seq[start:],codons)
                    print("ORF:3","\n","\nAmino acids sequence from nucleotide",x,"to",y,"in the 3rd ORF","\n"+"\n".join(textwrap.wrap(protein,60)).upper()) 
                    if protein=="":
                        print('No ORF found, please try again') 

                elif orf_query=="": ##----ALL------ORFs
                    codons=Codons()

                    seq1=seq[0:] ##----for the first ORF
                    protein1=""
                    for i in range(0,len(seq),3):
                        if seq1[i:i+3]=="atg":
                            start=seq1.find("atg")
                            protein1+=codonToProtein(seq1[start:],codons)
                    print("ORF:1","\n","\nAmino acids sequence from nucleotide",x,"to",y,"in the 1st ORF","\n"+"\n".join(textwrap.wrap(protein1,60)).upper())
                    if protein1=="":
                        print('No ORF found, please try again')            
                    
                    seq2=seq[1:] ##---for the second ORF
                    protein2=""
                    for i in range(0,len(seq),3):
                        if seq2[i:i+3]=="atg":
                            start=seq2.find("atg")
                            protein2+=codonToProtein(seq2[start:],codons)
                    print("ORF:2","\n","\nAmino acids sequence from nucleotide",x,"to",y,"in the 2nd ORF","\n"+"\n".join(textwrap.wrap(protein2,60)).upper())
                    if protein2=="":
                        print('No ORF found, please try again') 

                    seq3=seq[2:] ##----for the third ORF
                    protein3=""
                    for i in range(0,len(seq),3):
                        if seq3[i:i+3]=="atg":
                            start=seq3.find("atg")
                            protein3+=codonToProtein(seq[start:],codons)
                    print("ORF:3","\n","\nAmino acids sequence from nucleotide",x,"to",y,"in the 3rd ORF","\n"+"\n".join(textwrap.wrap(protein3,60)).upper()) 
                    if protein3=="":
                        print('No ORF found, please try again') 
                range_query=input("Enter range e.g [3,2) or (3,2) or (3,2] or [3,2] for print out of nucleotides (Blank line to Exit) : ")

##Small glitch, you can enter other ranges after FULL, but if you enter FULL after other ranges, the program breaks,not sure how to fix it

#####-------------------------F for Features----------------------------------------------################

    if query=="F":
         feature_query=input("Chooose the type of feature query P(Position) or N(Name) or Empty space for Summary: ")
         while feature_query!="":                    

             if feature_query=="N": ##-----------------------------if name is entered
                 name_query=input("Enter the name of the feature: ")
                 name_query=name_query.lower()

                 if name_query=="source": ##-----if source is entered
                     print("Searching for features with name",name_query,"...")
                     for i in range(len(genbank["FEATURES"][1]['source'])):
                         print("Feature",i+1,"of",len(genbank["FEATURES"][1]['source']))
                         for item in genbank["FEATURES"][1]['source'][i]:                
                             print("\t",item)       
                     
                 elif name_query=="cds": ##-----if cds is entered
                     print("Searching for features with name",name_query,"...")
                     for i in range(len(genbank["FEATURES"][2]["CDS"])):
                         print("Feature",i+1,"of",len(genbank["FEATURES"][2]["CDS"]))
                         for item in genbank["FEATURES"][2]["CDS"][i]:                
                             print("\t",item)
                     
                 elif name_query=="gene": ##----if gene is entered
                     print("Searching for features with name",name_query,"...")
                     for i in range(len(genbank["FEATURES"][3]["GENE"])):
                         print("Feature",i+1,"of",len(genbank["FEATURES"][3]["GENE"])) 
                         for item in genbank["FEATURES"][3]["GENE"][i]:                
                             print("\t",item)
                         
             elif feature_query=="P": ###-----------------------------------if position is entered
                        
                 keyword='..'
                 datar="".join(features_list)
                 nsource=datar.count(keyword)
                 keylocs=[]
                 k=0
                 for i in range(nsource):
                     t=datar.find(keyword,k)
                     keylocs.append(t)
                     k=t+10
                 loc_list=[]
                 for j in range(len(keylocs)-1):
                     loc_list+=datar[keylocs[j]-5:keylocs[j]+7].split()
                 #print(loc_list)

                 new_loc_list=[]
                 temp=""
                 temp2=""
                 temp3=""
                 temp4=""
                 for item in loc_list:
                     temp=item.replace("..",",")
                     temp2=temp.replace("<","")
                     temp3=temp2.replace("(","")
                     temp4=temp3.replace(")","")
                     new_loc_list+=[temp4]   
                 #print(new_loc_list)

                 range_list=[]
                 for item in new_loc_list:
                     endp=item.find(",")
                     x=int(item[0:endp])
                     y=int(item[endp+1:])
                     range_list+=[range(x,y)]
                 #print(range_list)
                 #[range(1, 5028), range(1, 206), range(687, 3158), range(687, 3158), range(3300, 4037)]

                 position_query=input("Enter a range in the format e.g [687-3158] to see features: ")
                 endz=position_query.find(",")
                 originz=position_query.find(",")
                 a=int(position_query[1:endz])  
                 b=int(position_query[originz+1:-1])
                 #print((a,b))

                 output_list=["\n\t".join(genbank["FEATURES"][1]['source'][0]),"\n\t".join(genbank["FEATURES"][2]["CDS"][0]),"\n\t".join(genbank["FEATURES"][3]["GENE"][0]),"\n\t".join(genbank["FEATURES"][2]["CDS"][1]),"\n\t".join(genbank["FEATURES"][3]["GENE"][1]),"\n\t".join(genbank["FEATURES"][2]["CDS"][2])] #I failed to automate this, made the output list manually :/

                 print("Search for Features in range",[a,b],"...")
                 for j in range(len(range_list)):
                     if a in range_list[j] and b in range_list[j]:
                         print("Features in",j+1,"of",j+1)
                         print(output_list[j])

             feature_query=input("Chooose the type of feature query P(Position) or N(Name) or Empty space for Summary: ")

######-------------------------------------E for export--------------------------------------------##################

    if query=="E":
        
        fasta_query=input("Enter name of fasta file, (.fasta or .fa), and directory where you want it created (Empty space for Summary): ")
        while fasta_query!="":
            if os.path.exists(fasta_query)==True:
                print('****WARNING file directory already exists***')
            else:
                system_warning=input("press Enter if you wish to proceed and create the fasta file: ")
                if system_warning=="":
                    fasta_file=open(fasta_query,'a')
                    fasta_file.writelines("\n".join(textwrap.wrap(">gi|{0}|ref|{1}|{2}".format(genbank['VERSION'][1][3:],genbank['ACCESSION'],genbank['DEFINITION']),70)))
                    fasta_file.writelines("\n"+"\n".join(textwrap.wrap(genbank['ORIGIN'],70)).upper())
                    fasta_file.close()
            fasta_query=input("Enter name of fasta file, (.fasta or .fa), and directory where you want it created(Empty space for Summary): ")



########----------------------------------Q for quit----------------------------------------------#####################

    if query=='Q':
        quit_query=input("Do you want to exit(E) or do you want to load another file(F): ")
        if quit_query=='E':
            break
        elif quit_query=='F':
            filename=input("Enter file path to load new file: ")



    a="="*60
    print()
    print('GBK Reader-({})DNA'.format(filename),"\n"+a)
    print("Sequence:",genbank["ACCESSION"],"("+genbank["LOCUS"][0]+",",genbank["LOCUS"][1]+genbank["LOCUS"][2]+")")
    print("Description: "+genbank["DEFINITION"]) #--I changed Description so that it's more informative,the original as per instructions  
    print("Source: "+genbank["SOURCE"][0])
    print("Number of References:",len(genbank["REFERENCE"]))
    print("Number of Features:",(len(genbank["FEATURES"][1]["source"])+len(genbank["FEATURES"][2]["CDS"])+len(genbank["FEATURES"][3]["GENE"])),"\n"+a) 
    query = input("R:References S:Sequence M:Motif T:Translate F:Features E:Export Q:Quit > ")

