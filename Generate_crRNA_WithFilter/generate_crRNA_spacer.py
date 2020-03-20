import os
import sys
from Bio.SeqUtils import GC
from Bio.Seq import Seq

def DNA2RNA(s):
    basecomplement = {'T': 'U', 'C': 'C', 'G': 'G', 'A': 'A'}
    letters = list(s)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)

inf = sys.argv[1]
seq_col = int(sys.argv[2]) -1
name_col = int(sys.argv[3]) -1
outf = sys.argv[4]
out = open(outf, "w")
out.write("%s\t%s\t%s\t%s\t%s\t%s\n" %("name","spacer_DNA","spacer_RNA","Genome_DNA","Genome_RNA","GC%"))
for line in open(inf):
        cols = line.rstrip().split("\t")
        out.write("%s\t" %(cols[name_col]))
        Genome_DNA = cols[seq_col]
        if "AAAA" in Genome_DNA:
            continue
        spacer_DNA = Seq(Genome_DNA).reverse_complement()
        Genome_RNA = DNA2RNA(Genome_DNA)
        spacer_RNA = DNA2RNA(spacer_DNA)
        out.write("%s\t%s\t%s\t%s\t%.2f\n"  %(spacer_DNA,spacer_RNA, Genome_DNA, Genome_RNA, GC(cols[0])))
out.close()
