from utils import from_pickle, to_json
from Bio.Seq import Seq
import os


def diverse_get_guide(guides, fingerprints):
    ordered_guides = sorted(
        [(len(guides[guide]), guide) for guide in guides], key=lambda a: a[0]
    )
    top_num_covered, _ = ordered_guides[-1]
    top_guides = [
        guide for guide in fingerprints if len(guides[guide]) == top_num_covered
    ]

    return top_guides[0]


def remove_seqnames_covered(guide_to_seqname, seqnames_covered):
    new_guides = {}
    for guide in guide_to_seqname:
        hits = guide_to_seqname[guide]
        new_hits = hits.difference(seqnames_covered)
        new_guides[guide] = new_hits
    return new_guides


def main(guide_candidates_fname, sorted_guides_fname, final_guides_fname):
    sorted_guides = from_pickle(sorted_guides_fname)

    guide_to_seqnames = from_pickle(guide_candidates_fname)

    print("Creating minimal guide set")
    data = []
    all_seqnames = {
        seqname
        for _, seqname_list in guide_to_seqnames.items()
        for seqname in seqname_list
    }
    print("Num seqnames: {}".format(len(all_seqnames)))
    seqnames_covered = set()
    while len(seqnames_covered) < len(all_seqnames):
        guide_to_seqnames = remove_seqnames_covered(guide_to_seqnames, seqnames_covered)
        guide = diverse_get_guide(guide_to_seqnames, sorted_guides)

        hits = guide_to_seqnames[guide]

        seqnames_covered.update(hits)

        guide = Seq(guide).reverse_complement()
        guide = str(guide)

        data.append(
            {"guide": guide, "cumulative_sequences_covered": len(seqnames_covered)}
        )

        print(
            "Cumulative Num covered: {} out of {}".format(
                len(seqnames_covered), len(all_seqnames)
            )
        )

    to_json(final_guides_fname, data)


if __name__ == "__main__":
    pass
