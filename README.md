# nCov2019_Guide_Design
## 1. Design effective and specific crRNAs for nCov2019, MERS and SARS
**Detect 22nt sequences in conserved region (Perfect match COVID-19 <=1 mismatch SARS/MERS)**
```
python horizontal-pool/main.py sequence_file.fasta -o ./output_data
```
**Remove Off-target in human transcriptome by using bowtie**
```
bowtie -a -S Human_GRCh38_Transcriptome_BowtieIndex nCov_22nt_seqs.fq nCov_22nt_seqs_OffTarget_HG38_RNA.sam -v 2
python Summarize_OffTarget.py nCov_22nt_seqs_OffTarget_HG38_RNA.sam Total_RNA_Number 0 nCov_22nt_seqs_OffTarget_Summary.txt
```
**Generate crRNA space sequences and filter "TTTT"**
```
python generate_crRNA_spacer.py nCov_22nt_seqs_NoOffTarget.txt colnum_22nt_Seqs Colnum_22nt_Seqs_Names Final_crRNA.output
```

## 2. Design pan-coronavirus crRNAs
**Collect 22nt unique sequences for all known CoV genomes and generate a minimum pool of 22 crRNAs for targeting all CoV genomes**
```
python minipool/main.py sequence_file.fasta -o ./output_data
```
**Remove Off-target in human transcriptome by using bowtie**
```
bowtie -a -S Human_GRCh38_Transcriptome_BowtieIndex nCov_22nt_seqs.fq nCov_22nt_seqs_OffTarget_HG38_RNA.sam -v 2
python Summarize_OffTarget.py nCov_22nt_seqs_OffTarget_HG38_RNA.sam Total_RNA_Number 0 nCov_22nt_seqs_OffTarget_Summary.txt
```
**Generate crRNA space sequences and filter "TTTT"**
```
python generate_crRNA_spacer.py nCov_22nt_seqs_NoOffTarget.txt colnum_22nt_Seqs Colnum_22nt_Seqs_Names Final_crRNA.output
```
