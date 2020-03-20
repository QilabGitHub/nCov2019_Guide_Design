from Bio import SeqIO
from collections import Counter
from pprint import pprint
from matplotlib import pyplot as plt
import numpy as np
import argparse


def get_guides(
    output_root,
    consensus_percents,
    empty_spaces,
    alignment_length,
    consensuses,
    cutoff,
    guide_length=22,
):
    with open("{}/guides.txt".format(output_root), "w") as wopen:
        for i in range(alignment_length):
            if empty_spaces[i]:
                continue

            def filled_spaces(i, j):
                new_seq = empty_spaces[i:j]
                return len(new_seq) - sum(new_seq)

            j = i + 22
            while filled_spaces(i, j) < 22 and j < alignment_length:
                j += 1

            if filled_spaces(i, j) < 22 and j >= alignment_length:
                continue

            if not all([elem >= cutoff for elem in consensus_percents[i:j]]):
                continue

            guide = "".join(consensuses[i:j])
            guide = guide.replace("-", "")
            if "N" in guide:
                continue

            wopen.write("{}\t{}\t{}\n".format(guide, i, j))


def plot_conservation(
    output_root, consensus_percents, alignment_length, wing_length=500
):
    mean_values = []

    for idx in range(wing_length, alignment_length - wing_length):
        wings = consensus_percents[idx - wing_length : idx + wing_length]
        mean_value = np.mean(np.array(wings))
        mean_values.append(mean_value)

    parsed_mean_values = np.array(mean_values)

    plt.plot(
        list(range(wing_length, alignment_length - wing_length, parsed_mean_values))
    )
    plt.xlim([0, alignment_length])
    plt.ylabel("% conservation")
    plt.xlabel("Nucleotide position along reference sequence")
    plt.savefig("{}/conservation.pdf".format(output_root))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_sequence", help="Nucleotide alignment formatted as a fasta file",
    )
    parser.add_argument("-o", "--output_root", default=".")
    parser.add_argument("-c", "--cutoff", default=1)

    args = parser.parse_args()
    input_sequence = args.input_sequence
    output_root = args.output_root
    cutoff = args.cutoff

    sequences = []
    for seq_record in SeqIO.parse(input_sequence, "fasta"):
        sequences.append(str(seq_record.seq))
    alignment_length = len(sequences[0])

    empty_spaces = []
    consensus_percents = []
    consensuses = []
    for i in range(alignment_length):
        all_position_values = [seq[i] for seq in sequences]
        position_values = [elem for elem in all_position_values if elem != "-"]

        empty_space = 0
        consensus_percent = 0
        consensus = "N"

        if len(position_values) > 0:
            position_values_counter = Counter(position_values)
            most_common_value, num_occurences = position_values_counter.most_common(1)[
                0
            ]

            if num_occurences >= (len(all_position_values) / 2):
                consensus = most_common_value
                consensus_percent = num_occurences / len(all_position_values)
        else:
            consensus_percent = 1
            empty_space = 1

        empty_spaces.append(empty_space)
        consensus_percents.append(consensus_percent)
        consensuses.append(consensus)

    get_guides(
        output_root,
        consensus_percents,
        empty_spaces,
        alignment_length,
        consensuses,
        cutoff,
    )
    plot_conservation(output_root, consensus_percents, alignment_length)


if __name__ == "__main__":
    main()
