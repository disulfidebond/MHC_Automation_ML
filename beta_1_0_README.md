## README for MHC Haplotyper Using Machine Learning

### Overview
This is the first beta release of the MHC haplotyper using Machine Learning. Briefly, it uses a training set, created from researcher-created pivot tables, for a Machine Learning (ML) Classifier to predict haplotypes.

Usage is described in the "Usage" section; most users should start here. 

The "Release Notes" provides technical information, and information on what will be added/improved next. Unless you are specifically interested in learning about Machine Learning, or if you are curious about new features that will be added, this section can be skipped by most users.

### Usage
To use the MHC Haplotyper, download the zipped file from [Experiment 21380](https://dholk.primate.wisc.edu/project/dho/experiments/21380/begin.view?), OR download the jupyter notebook named ML_MHC_haplotyper_beta_1_0.ipynb and copy the following files into the same folder as the python notebook:
* training.txt (note: this must be the training.txt file from the current github beta branch or from Experiment 21380)
* allele_list.txt (note: this must be the allele_list.txt from the current github beta branch, or from Experiment 21380) 

Then, open the python notebook by opening Terminal on Mac OSX and typing:

        jupyter notebook 
        # or type jupyter lab

Finally, follow the directions in the notebook. Do **not** simply run the notebook from start to finish without reading the instructions in the notebook.

At this point, the Automation only predicts Haplotypes for MHC-A and MHC-B. Briefly, the current version scans alleles, and makes a prediction regarding the haplotype. If a haplotype is encountered that has not been added to the training set, this will produce a 'Warning' error messgae, and the data for that sample will simply be passed along to the researcher for assessment.
* This behavior is limited to this version (1_0) only.  See Release Notes for more information
* Expanding to other Haplotypes will be addressed in a future build/version.
* Expanding to other types of data, such as PacBio and WholeExome, will begin to be addressed in the next version.


### Release Notes
The current release is the first version of an Automated Haplotyper using Machine Learning. Its purpose is to improve efficiency in the workflow, where the initial input is a pivot table or read counts from a pivot table, and the output is a pivot table that is verified by a researcher.
The next version of the Automated Haplotyper will use a Neural Network (NN) with Deep Learning (DNN), as opposed to the current Machine Learning Classifier, to addres multiple issues, including accuracy and expansion.
* See [Developer Pre-Release Notes 1](https://github.com/disulfidebond/MHC_Automation_ML/blob/dev/beta_1_0_prerelease_1.md) and [Developer Pre-Release Notes 2](https://github.com/disulfidebond/MHC_Automation_ML/blob/dev/beta_1_0_prerelease_2.md) for a detailed explanation.

The next version, 1.1 (the same as 1_1), will address bugfixes and the following:
* replace parser that creates training data with a standalone, edited, and documented parser.
  * This will be the first "development" tool, and is not designed to be used as part of a python notebook, since the training set must already be created.
* replace ML Classifier with a Deep Neural Network (DNN) that uses backpropagation to increase accuracy and account for unknown alleles and Haplotypes
* Increase accuracy above 92% as measured by cross-validation
