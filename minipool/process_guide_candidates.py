from Bio import SeqIO
from collections import defaultdict
from pprint import pprint
import os
from glob import glob
from utils import to_pickle, from_pickle
import re


def main(input_fname, output_fname):
    guide_to_seqname = from_pickle(input_fname)
    guide_to_seqname = {
        guide: seqname
        for guide, seqname in guide_to_seqname.items()
        if "aaaa" not in guide.lower()
    }
    to_pickle(output_fname, guide_to_seqname)


if __name__ == "__main__":
    pass
