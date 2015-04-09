def read_fasta(filename):
    name = None
    name2seq = {}
    for line in open(filename):
        if line.startswith(">"):
            if name:
                name2seq[name]=seq
            name=line[1:].rstrip()
            seq=""
        else:
            seq+=line.rstrip()
    name2seq[name]=seq
    return name2seq

x=read_fasta("sequence.fasta")
print x