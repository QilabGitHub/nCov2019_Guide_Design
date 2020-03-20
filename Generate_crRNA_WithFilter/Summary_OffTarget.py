import os
import sys

inf_sam = sys.argv[1]
genome_num = float(sys.argv[2])
strand_direction = int(sys.argv[3]) ####Flag in sam file; 16--> SEQ being reverse complemented 0--> SEQ just mapped to the reference
outf = sys.argv[4]

sgrna_dict0 = {}
sgrna_dict1 = {}
sgrna_dict2= {}
sgrna_dict3= {}
for line in open(inf_sam):
        if line.startswith("@"):
                continue
        else:
                cols = line.strip().split("\t")
                sgrna_name = cols[0]
                mapping_status = int(cols[1])
                genome_name = cols[2]
                mismatch = int(cols[11].split(":")[2])
                if not sgrna_dict0.has_key(sgrna_name):
                        sgrna_dict0[sgrna_name] = []
                        sgrna_dict1[sgrna_name] = []
                        sgrna_dict2[sgrna_name] = []
                        sgrna_dict3[sgrna_name] = []
                if mapping_status != strand_direction:
                        continue
                if mismatch == 0:
                        sgrna_dict0[sgrna_name].append(genome_name)
                if mismatch == 1:
                        sgrna_dict1[sgrna_name].append(genome_name)
                if mismatch == 2:
                        sgrna_dict2[sgrna_name].append(genome_name)
                if mismatch == 3:
                        sgrna_dict3[sgrna_name].append(genome_name)
out = open(outf,"w")
out.write("sgRNA_name\t#TargetGenome(Total)\t#TargetGenome(0Mismatch)\t#TargetGenome(1Mismatch)\t#TargetGenome(2Mismatch)\t#TargetGenome(3Mismatch)\tTargetGenome(0Mismatch)\tTargetGenome(1Mismatch)\tTargetGenome(2Mismatch)\tTargetGenome(3Mismatch)\n")
for key in sgrna_dict0.keys():
        out.write("%s" %key)
        out.write("\t%d(%.2f%s)" %(len(sgrna_dict0[key])+len(sgrna_dict1[key])+len(sgrna_dict2[key])+len(sgrna_dict3[key]),
                (len(sgrna_dict0[key]) +len(sgrna_dict1[key])+len(sgrna_dict2[key])+len(sgrna_dict3[key]))/genome_num*100, "%"))
        out.write("\t%d(%.2f%s)" %(len(sgrna_dict0[key]), len(sgrna_dict0[key])/genome_num*100, "%"))
        out.write("\t%d(%.2f%s)" %(len(sgrna_dict1[key]), len(sgrna_dict1[key])/genome_num*100, "%"))
        out.write("\t%d(%.2f%s)" %(len(sgrna_dict2[key]), len(sgrna_dict2[key])/genome_num*100, "%"))
        out.write("\t%d(%.2f%s)" %(len(sgrna_dict3[key]), len(sgrna_dict3[key])/genome_num*100, "%"))
        out.write("\t%s" %(";;".join(sgrna_dict0[key])))
        out.write("\t%s" %(";;".join(sgrna_dict1[key])))
        out.write("\t%s" %(";;".join(sgrna_dict2[key])))
        out.write("\t%s" %(";;".join(sgrna_dict3[key])))
        out.write("\n")
out.close()
