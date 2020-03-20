from Bio import SeqIO
from collections import defaultdict
from pprint import pprint
import os
from glob import glob
from utils import to_pickle
import re


def main(input_fnames, output_fname):
    fnames = []
    for input_sequence in input_fnames:
        fnames.extend(glob(input_sequence))

    name_to_seqs = defaultdict(list)
    for fname in fnames:
        for seq_record in SeqIO.parse(fname, "fasta"):
            sequence = str(seq_record.seq).replace("-", "")
            name_to_seqs[seq_record.name].append(sequence)

    print("Creating database")
    guide_to_seqname = defaultdict(set)
    for seqname, sequences in name_to_seqs.items():
        for sequence in sequences:
            for i in range(len(sequence) - 22):
                guide = sequence[i : i + 22]
                guide_to_seqname[guide].add(seqname)

    to_pickle(output_fname, guide_to_seqname)


if __name__ == "__main__":
    pass
