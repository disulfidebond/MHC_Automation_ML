### Beta Release 1.0.1 Supplemental Comment
#### Author: JRC

After attempting to run the python notebook with Roger, three facts became immediately clear:
* I had been using the wrong format of Excel pivot tables as a model for inputting data
* It would take a lot of work to update the code to accept output from Dave O'Connor's pipeline
* Any work to change the type of file that the python notebook accepts to format the data as needed would inevitably turn into a game of "whack-a-mole", because even a standardized format would not account for archived analyses and typos within the Excel spreadsheets

An idea that has been back-burnered was to modify a Natural Language Processing (NLP) Deep Neural Network (DNN).  This approach would create a corpus of text using the file names, genotype and haplotype names, and other relevant data within the files, with the end goal being to train the DNN to recognize ambiguity better than what regular expressions would accomplish.

This approach is not without its hazards. NLP is ten steps beyond complicated, as [Google](https://ai.google/research/pubs/?area=NaturalLanguageProcessing) and [Facebook](https://research.fb.com/publications/?cat=8) have both attested; and unlike the NN that will be deployed for the Classifier, success is not guaranteed for this approach, and critically, work from this approach could become a dead-end that could not be applied to other projects and work for GS.  For the moment, I'm going to "punt" on deciding whether of not to pursue NLP.

The 1.0.1 update partially addressed compatibility for pivot tables that were created from Dave O'Connor's pipeline; they must be converted to a csv file.  Future builds will address compatibility with these files, either through tortuously convoluted logic (this is the current approach), or through the above-described NLP.

