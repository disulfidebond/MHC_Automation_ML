### Beta Release 1.0 Supplemental Comment
#### Author: JRC

At this point, there is one remaining roadblock, and unfortunately it is a big one.

In the current beta 1_0 build, if you run it, it will fail with the error 

> Singleton array array(None, dtype=object) cannot be considered a valid collection.

This is caused by code a few cells back, and it was written this way for a very specific reason.

The function valuesToTestList() is set up to label values, but if it encounters a value from the input (or testing dataset) that it hasn't encountered yet, then it acts as a 'circuit breaker', and immediately stops everything by returning None. (Note this behavior is not intended for final release.)

The reason for this behavior will be made clear shortly.  Currently, the classifier trains based on two types of values, either a single haplotype, for example 'A001', or a pair of haplotypes, for example 'A001-A002', for a given set of genotypes that have already been evaluated by a human researcher.  

The MHC Complex is very diverse, and for example if there are 20 possible Haplotypes, then the possible number of Haplotypes could be calculated as a combination with repetition, since a haplotype could be homozygous or heterozygous:

        Possible_Haplotype_Combinations = (r + n - 1)/{r!(n-1)!}
        where
        r = number of haplotypes per sample, 2
        n = total number of possible haplotypes, in this abbreviated example 20

Note that this **could** also be calculated as a permutation without repetition.  In the code, repeated haplotype labels are renamed as a single label, and repeats are not allowed ('A001-A002' is the same as 'A002-A001')
But, you'd have to calculate the homozygous alleles separately and add them in:

        Possible_Haplotype_Permutations = n!/{r!(n-r)!} + n
        where
        r = number of haplotypes per sample, 2
        n = total number of possible haplotypes, in this abbreviated example 20

I'll leave it as an exercise to the reader to show not only that the above two equations are equal, but that they are correct for a set of Haplotypes X1 and X2. 

In a research setting, this diversity will have limits, which will make some calculations easier.  For example, with Mafa NHP, there is very little divergence, so although both of the above equations are correct, there is very little chance of encountering a new haplotype or new genotype.  In other datasets, there is an increased chance of encountering a new haplotype or genotype.

To handle this problem, there are several strategies, all of which have benefits and disadvantages, and none of which are a "one size fits all" approach. One option has already been discussed in Developer comments is to create a Convolutional Neural Network (CNN) that will be able to draw enhanced correlations from the dataset, but this will take additional time to build, due in no small part to its complexity.  

Another option, also discussed in Developer comments, is to expand the current training set to reduce the probability that the classifier will encounter a Haplotype pair that has not been entered.  However, the current dataset has 130 Haplotypes for MHC-A, whereas if there are 57 possible alleles for Haplotype A, using the above calculations:

        r = 2
        n = 57
        Possible_Haplotype_Combinations = (57 + 2 - 1)/{2!(57 - 1)!} = (58!/{2!(56)!}) = 1653
        training data pairings listed = 130/1653 = 7.9%

Which clearly shows the need for a more robust approach, even in the short term before a CNN is implemented.

Toward that end, I'm adopting my usual reusable and multi-use approach with the following 2 methods, both or either of which may be used.  Neither of these methods will substitute data from researchers--only supplement missing datapoints--and as much as possible, data from experiments should (will) be used first to complete a training dataset.

#### Method 1: Datamining

After consulting with Roger, Hadjer, and Ryan, all have noted that a haplotype can be called without matching to all alleles; in fact, it is somewhat common for a haplotype to be called when it matches to only one.  These specific alleles are denoted as "Diagnostic" alleles.  

The first method to clear the roadblock involves datamining the existing data to count the number of times a haplotype h is called when it is matched with 1,2,...,n alleles, these counts can be modeled as a poisson distribution:


        P(X=k) = {(𝝺^k)(e^-𝝺)}/k!
        
* see https://www.nature.com/articles/ng.3257
* see also https://onlinecourses.science.psu.edu/stat504/node/57/
* in this context, for each haplotype, there will be k events that correspond to the number of alleles that successfully matched and were called for a haplotype and lambda is the average rate for the number of matches per haplotype, for k > 0

  * **note** that this will vary between haplotypes, however, the probability for matching for each haplotype is independent, thereby still following the assumptions for a poisson distribution 

Once the probability for the number of each alleles that match is obtained, it can be used to create a probable number of genotype matching for each haplotype.
        


#### Method 2: Table Joins
For this method, I'll consult with Dave Baker heavily, as he is much more proficient with SQL and no-SQL than I am.  

Given an input dataset of labels as column names, and one-hot vectors as row/column values:

| genotype        | 'A001-A002'           | 'A001'  | 'A002'
| ------------- |-------------:| -----:|--------:|
| A_01 | 0 | 0 | 0 |
| A_02 | 1 | 1 | 0 |
| A_03 | 0 | 0 | 0 |
| A_04 | 1 | 0 | 1 |
| A_05 | 0 | 0 | 0 |

A left outer join would produce the following result for each column:

| genotype        | 'A001-A002'           | 'A001'  |
| ------------- |-------------:| -----:|
| A_01 | 0 | 0 | 
| A_02 | 1 | 1 | 
| A_03 | 0 | 0 | 
| A_04 | 1 | NULL |
| A_05 | 0 | 0 |

| genotype        | 'A001-A002'           | 'A002'  |
| ------------- |-------------:| -----:|
| A_01 | 0 | 0 | 
| A_02 | 1 | NULL | 
| A_03 | 0 | 0 | 
| A_04 | 1 | 1 |
| A_05 | 0 | 0 |

The fictitious 'A_03' example above could be ambiguous for 'A001' and 'A002', but with reasonable certainty one could predict that 'A001' contained 'A_02' and 'A002' contained 'A04'.
Using existing data for a hypothetical pairing 'A001-A003', one could then infer the missing datapoints.

It should be noted that this proposed method serves two purposes: a 'stopgap' until a more advanced neural network can be created, and as the groundwork for the more advanced correlations used by the neural network.  
