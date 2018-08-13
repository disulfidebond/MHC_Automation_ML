# README for Alpha

## Initial commit

The initial commit for alpha contains the notes, comments, data files, and python notebooks that were used to create the current stable beta build.

Briefly, here is a description of each:

* ML_MHC_haplotyping_alpha1_0.ipynb
  * This file is a concatenated python notebook of the workflow that demontrated the proof of concept for ML for Haplotyping. It had several areas that critically needed revision, such as creating a streamlined workflow that was not hardcoded, before it would be ready for additional testing by researchers in Genetics Services.
* MHC_beta_prebuild_1_0.ipynb
  * This file is the beginning of work to assemble the automation workflow that ML would work within
* MHC_beta_prebuild_1_0.ipynb, MHC_beta_prebuild_1_1.ipynb
  * These two files were notes and code on creating a parser for the input data for ML, and ensuring that the User Interface would be as seamless as possible.
* MHC_beta_prebuild_1_2.ipynb
  * This file is essentially part 1 of the overall workflow, with some additional minor debugging still required
* allele_df-trainingSet-HapA, allele_df-testingSet-HapA
  * These were files that were used both for test datasets for ML, and as test input files for the parser.
* fParse.py, testLabKeyQuery.py
  * These tested the API for labkey and are a good template, regardless of the programming language
* parsedLabKeyMiSeqResults.txt
  * this is the *output* from the parser; the input file is a raw json format with all lab data, and for sensitivity/security reasons it was not included
* workflow_comments_filterParse.md
  * these are notes on how I created and formatted the input file for Machine Learning
