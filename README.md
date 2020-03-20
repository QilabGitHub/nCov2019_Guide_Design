# nCov2019_Guide_Design
## 1. Design effective and specific crRNAs for nCov2019, MERS and SARS
**Detect 22nt sequences in conserved region (Perfect match COVID-19 <=1 mismatch SARS/MERS)**
```
```
**Remove Off-target in human transcriptome by using bowtie**
```
bowtie -a -S Human_GRCh38_Transcriptome_BowtieIndex nCov_22nt_seqs.fq nCov_22nt_seqs_OffTarget_HG38_RNA.sam -v 2
```
**Generate crRNA space sequences and filter "TTTT"**
```
```

## 2. Design pan-coronavirus crRNAs
**Collect 22nt unique sequences for all known CoV genomes**
```
```
**Generate a minimum pool of 22 crRNAs for targeting all CoV genomes**
```
```
**Remove Off-target in human transcriptome by using bowtie**
```
```
**Generate crRNA space sequences and filter "TTTT"**
```
```
