
# Import
import os
import sys

# Input
bedFileName = "/work/eg474423/eg474423_Projects/trunk/Mtss/Input/region3.bed"
mpbsFileName = "/hpcwork/izkf/projects/egg/TfbsPrediction/Results/MPBSAWG/K562_Evidence/fdr_4.bed"
predLoc = "/hpcwork/izkf/projects/egg/TfbsPrediction/Results/Footprints/Predictions/K562/"

# Parameters
predList = ["HD_D13_ModelH1hesc","HD_D13_ModelK562","HD_D139_ModelH1hesc","HD_D139_ModelK562"]

# Fetching mpbs
outputMpbsFileName = "/work/eg474423/eg474423_Projects/trunk/Mtss/Results/region3/fdr_4.bed"
os.system("intersectBed -wa -a "+mpbsFileName+" -b "+bedFileName+" > "+outputMpbsFileName)

# Fetching predictions
for predFileName in predList:
    outputPredFileName = "/work/eg474423/eg474423_Projects/trunk/Mtss/Results/region3/"+predFileName+".bed"
    os.system("intersectBed -wa -a "+predLoc+predFileName+".bed -b "+bedFileName+" > "+outputPredFileName)


