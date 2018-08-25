# README for Beta 1.0

## Beta 1_0 release notes

## Requirements:
* python 3.6
* python notebook file ML_MHC_haplotyper_beta_1_0.ipynb
* the following files must be in the same directory as the python notebook:
  * allele_df-trainingSet-HapB.csv
  * allele_df-trainingSet-HapA.csv
  * allele_df-testingSet-HapA.csv
  * input pivot table (20411_Felber1-2_MHC-I_Haplotypes_23Mar18.xlsx has been provided as an example)
  * allele_names.txt

The file "experimentIDList.txt" has been provided as a reference but is not directly used.  This file lists all of the experiments that were referenced to create the training dataset.

## Usage:
* Follow instructions inside python notebook "ML_MHC_haplotyper_beta_1_0_release.ipynb"
* The python notebook can be run from the start, but this is not recommended.
* The python notebook will output 2 files for mhc-A and mhc-B predictions

## Technical Comments:
See Dev fork
