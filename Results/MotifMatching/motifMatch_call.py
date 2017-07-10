
# Import
import os

# Parameters
organism="--organism hg19"
fpr="--fpr 0.0005"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
rand_proportion="--rand-proportion 1"
#bigbed="--bigbed"

# Execution
inputMatrix = "/work/eg474423/eg474423_Projects/trunk/Mtss/Results/MotifMatching/exp_mat/exp_mat.txt"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/Mtss/Results/MotifMatching/Results_FDR_3.5/"
myL = "MTSS_ME"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 100:00 -M 12000 -S 100 -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+inputMatrix
os.system(clusterCommand)
# -P izkf

