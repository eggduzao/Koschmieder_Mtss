
# Import
import os
import sys

# Input
inList = ["Methylation_1_hg19", "Methylation_2_hg19", "Region_hg19"]
liftFileName = "./hg19ToMm9.over.chain.gz"

# Execution
for inName in inList:
  inFileName = "./"+inName+".bed"
  outFileName = "./"+"_".join(inName.split("_")[:-1])+"_mm9.bed"
  unFileName = "./"+"_".join(inName.split("_")[:-1])+"_unlifted.bed"
  os.system("liftOver "+inFileName+" "+liftFileName+" "+outFileName+" "+unFileName)


