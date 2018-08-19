### Beta Release 1.0 Supplemental Comment 3
#### Author: JRC
I ran into a critical problem when the finish line was in sight. The current workflow is as follows:
1) import input data
2) parse input data into Pandas Dataframe that mimics the pivot tables, where column1 is the genotype names, and the rows are populated with one-hot vectors.
3) transpose the input data so that the haplotype naming is now column 1 (or in the case of a raw pivot table, have null values)
4) import training data (already formatted and setup for the Machine Learning Classifier)
5) transpose the training data so that the genotype names are now the row values (X) and the haplotype names in column 1 are now the labels (Y)
6) train the Classifier with the training data, where X = row values from the pivot table as one-hot vectors, y = labels
7) (Optional) run an accuracy check with either a subset of the training data or a different pre-formatted file
8) Instruct the Classifier to predict labels using the input data
9) show result
10) add prediction to pivot table, then write a new file

At step 5, it failed--or crashed--because the rows and columns for the training data didn't match the rows and columns for the input data.
The data for previous test builds had always used the ordering of the genotypes from the training data. At a basic level, the fix was simple: 
* re-format the input data to match the row ordering of the genotype names
* transpose the dataframe, because now the number and ordering of rows will match

However, this would not be an effective long term solution.  The moment a researcher attempted to use a different dataset that was not correctly formatted,
the exact same problem would occur, with the only solution being to manually reformat the data using a collection of python, bash, and perl scripts. 
This scenario was an important concern that this workflow was designed to address, thereby making such a workflow self-defeating at best.

Several attempts were made to create a patch for this problem, bearing in mind that 
[the build for a Neural Network](https://github.com/disulfidebond/MHC_Automation_ML/blob/dev/dev_comments2_beta_1_0.md) would not use these steps at all:
* transpose the input data values before step 5 (failed: would require completely rewriting code, and this code will be totally replaced in the next version)
* create parallel workflows with the input dataset and the training dataset parsed separately (failed: the training data would still not match the input data)
* reverse the workflow so that the training data matched the input data (failed: now the training data would not match its formatting workflow, thereby tripling work)

Ultimately, the following workflow was created instead, which I believe will accomplish multiple goals at once, 
including work in other projects to standardize, organize, and upload data to LabKey:
1) import input data
2) parse input data into Data Object (see below)
3) import training data
4) parse training data into Data Object (see below)
5) create training dataset with the format
[Label: [one-hot-vector]]
from training data in Data Object
6) create input dataset with the same format as in step 5
7) train the Classifier with the training data, where X = one-hot-vector values, Y = Label values
8) Instruct the Classifier to predict labels using the formatted input data
9) Create a new pandas dataframe with the output values, then output this as a csv file

        Data Object: list of x1,x2,...,xN values
        where:
        SAMPLEINT == integer or string corresponding to the sample identifier of row 1 in the Excel Sheet
        MHC_A1,MHC_A2 == MHC haplotype call for MHC-A ; may also be None,None for a raw pivot table, and MHC_A1,None for a pivot table with a homozygous haplotype call
        MHC_B1,MHC_B2 == MHC haplotype call for MHC-B ; may also be None,None or MHC_B1,None, see MHC_A
        genotypeList == column 1 of the pivot table, with the header rows removed
        one-hot-vector-genotypeList == a one-hot vector of values from the pivot table read VERTICALLY, i.e. down the columns
        one-vector-list-genotypeList-horizontal == a one-hot vector of values from the pivot table read HORIZONTALLY, i.e. across the rows
        readCounts_list-vertical == read counts instead of a one-hot vector when the pivot table is read VERTICALLY, i.e. down the columns
        readCounts_list-horizontal == read counts instead of a one-hot vector when the pivot table is read HORIZONTALLY, i.e. across the rows

        each x value is:
        x = [
            {
                entry_SAMPLEINT : [
                    [MHC_A1,MHC_A2], 
                    [MHC_B1,MHC_B2],
                    [genotypeList], 
                    [one-hot-vector-genotypeList],
                    [one-vector-list-genotypeList-horizontal],
                    [readCounts_list-vertical], 
                    [readCounts_list-horizontal] 
                ]
            }
        ]

This data structure serves multiple purposes.  It enables the completion of the Machine Learning Classifier workflow, and creates 
a parsing "module" that can be used to organize data for schemas within LabKey.
