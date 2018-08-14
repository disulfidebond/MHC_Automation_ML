### Beta Release 1.0 Supplemental Comment 2
#### Author: JRC

After studying several sources, including [1-3] here is the plan going forward:
* Expand the current training dataset through 2017 using the existing parser and tools, in the alpha branch and refined in the dev branch
* Modify the existing code to have a catch that warns if an unknown Haplotype is encountered, it will set it aside and return it with no prediction made.
  * Advise that this behavior will be modified in beta 1_1 and later
* Release this build as version beta 1.0 (beta_1_0)
* In addition to any bugfixes that need to be addressed, beta_1_1 will address the following goals:
  * replace parser that creates training data with a standalone, edited, and documented parser.
    * This will be the first "development" tool, and is not designed to be used as part of a python notebook, since the training set must already be created.
  * replace ML Classifier with a Deep Neural Network (DNN) that uses backpropagation to increase accuracy and account for unknown alleles and Haplotypes
    * The training sample dataset will be created as follows.
      * Methods 1 and 2 described in the previous supplement will each be tested to determine their applicability and effect on accuracy
      * Our hypothesis is using existing data to create a poisson distribution will result in pseudo-replicates, which will be refined in backpropagation, i.e. combining both Method 1 and Method 2
      * Alternatively, establishing a prior that uses the existing datapoints may prove to be a better, if redundant and complicated solution
      i.e. a [modification](http://cybert.ics.uci.edu) of a naive Bayes approach
  * Increase accuracy above 92% as measured by cross-validation

Accomplishing all 3 goals will result in the release of beta_1_1



[1] Albon, Chris. "Machine Learning Cookbook with Python". c2018. OReilly Press.

[2] Géron, Aurélien. "Hands-On Learning with Scikit-Learn and TensorFlow". c2017. OReilly Press

[3] Sosnovshchenko, Alexander. "Machine Learning with Swift". c2018. Packt Publishing.

[4] Baldi, P. and Long, A.D., "A Bayesian Framework for the Analysis of Microarray Expression Data: Regularized t-Test and Statistical Inferences of Gene Changes", Bioinformatics, 17, 6, 509-519, (2001)
