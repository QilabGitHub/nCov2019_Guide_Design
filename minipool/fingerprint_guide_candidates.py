from utils import to_pickle, from_pickle
import os


def fingerprint(guide):
    fingerprint = [0 for i in range(len(guide))]
    curr = guide[0]
    curr_len = 1
    for i in range(1, len(guide)):
        if guide[i] == curr:
            curr_len += 1

        if guide[i] != curr or i == len(guide) - 1:
            if curr_len > 1:
                fingerprint[curr_len - 1] += 1
            curr = guide[i]
            curr_len = 1
    return "".join(reversed([str(elem) for elem in fingerprint]))


def main(input_fname, output_fname):
    guide_to_seqnames = from_pickle(input_fname)

    fingerprinted_guides = [
        (fingerprint(guide), guide) for guide in guide_to_seqnames.keys()
    ]
    fingerprinted_guides.sort(key=lambda a: a[0])
    sorted_guides = [guide for _, guide in fingerprinted_guides]

    to_pickle(output_fname, sorted_guides)


if __name__ == "__main__":
    pass
