import argparse
import os
import prepare_guide_candidates
import process_guide_candidates
import fingerprint_guide_candidates
import set_cover


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_sequences",
        nargs="+",
        help="One or more fasta files. Aligned sequences are accepted (gap characters such as '-' are automatically removed). File paths are expanded using glob()",
    )
    parser.add_argument("-o", "--output_root", default=".")

    args = parser.parse_args()
    input_sequences = args.input_sequences
    output_root = args.output_root

    if not os.path.exists(output_root):
        os.makedirs(output_root)

    all_guide_candidates_fname = "{}/guide_candidates.pickle".format(output_root)
    processed_guide_candidates_fname = "{}/guide_candidates.pickle".format(output_root)
    sorted_guides_fname = "{}/sorted_guide_candidates.pickle".format(output_root)
    final_guides_fname = "{}/final_guides.json".format(output_root)

    if not os.path.exists(all_guide_candidates_fname):
        print("Preparing guide candidates")
        prepare_guide_candidates.main(input_sequences, all_guide_candidates_fname)

    if not os.path.exists(processed_guide_candidates_fname):
        print("Processing guide candidates")
        process_guide_candidates.main(
            all_guide_candidates_fname, processed_guide_candidates_fname
        )

    if not os.path.exists(sorted_guides_fname):
        print("Fingerprinting and sorting guide candidates")
        fingerprint_guide_candidates.main(
            processed_guide_candidates_fname, sorted_guides_fname
        )

    if not os.path.exists(final_guides_fname):
        print("Doing set cover")
        set_cover.main(
            processed_guide_candidates_fname, sorted_guides_fname, final_guides_fname
        )


if __name__ == "__main__":
    main()
