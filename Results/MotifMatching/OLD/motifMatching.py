
# Import
import os
import sys

###########################################
# Parameters
###########################################

coord_file="-coord_file=/work/eg474423/eg474423_Projects/trunk/Mtss/MotifMatching/Input/coordinate.bed"
#motif_list="-motif_list="
#gene_list="-gene_list="
#assoc_coord_file="-assoc_coord_file="
#mpbs_file="-mpbs_file="
#mpbs_final_file="-mpbs_final_file="

#genome_list="-genome_list="
#association_file="-association_file="
#chrom_sizes_file="-chrom_sizes_file="
pwm_dataset="-pwm_dataset=/hpcwork/izkf/projects/huvec_inflammation/motif_enrichment/Input/PWM/"
logo_location="-logo_location=../../../logo/"
random_coordinates="-random_coordinates=/work/eg474423/eg474423_Projects/trunk/Mtss/MotifMatching/Input/random.bed"

organism="-organism=hg19"
motif_match_fpr="-motif_match_fpr=0.001"
motif_match_precision="-motif_match_precision=10000"
motif_match_pseudocounts="-motif_match_pseudocounts=0.0"
#multiple_test_alpha="-multiple_test_alpha="
#promoter_length="-promoter_length="
#maximum_association_length="-maximum_association_length="
#cobinding="-cobinding="
#cobinding_enriched_only="-cobinding_enriched_only="
#enriched_pvalue="-enriched_pvalue="
#rand_proportion_size="-rand_proportion_size="
all_coord_evidence="-all_coord_evidence=Y"

output_location="-output_location=/work/eg474423/eg474423_Projects/trunk/Mtss/MotifMatching/Results_FDR_3/"
print_association="-print_association=N"
print_mpbs="-print_mpbs=Y"
print_results_text="-print_results_text=N"
print_results_html="-print_results_html=N"
print_enriched_genes="-print_enriched_genes=N"
print_rand_coordinates="-print_rand_coordinates=N"
print_graph_mmscore="-print_graph_mmscore=N"
print_graph_heatmap="-print_graph_heatmap=N"

###########################################
# Execution
###########################################

clusterCommand = "bsub "
clusterCommand += "-J MTE -o MTE_out.txt -e MTE_err.txt "
clusterCommand += "-W 200:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifStatistics_pipeline.zsh "
clusterCommand += coord_file+" "+pwm_dataset+" "+logo_location+" "+random_coordinates+" "
clusterCommand += organism+" "+motif_match_fpr+" "+motif_match_precision+" "+motif_match_pseudocounts+" "+all_coord_evidence+" "
clusterCommand += output_location+" "+print_association+" "+print_mpbs+" "+print_results_text+" "+print_results_html+" "
clusterCommand += print_enriched_genes+" "+print_rand_coordinates+" "+print_graph_mmscore+" "+print_graph_heatmap
os.system(clusterCommand)


