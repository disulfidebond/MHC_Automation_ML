# Methods:

Part I:
* parsed data from LabKey API using python with the command below
  * *Comment from JC: The syntax for a query to LabKey is nearly the same for Python, R, Perl, and Java. At a basic level, you must either use a netrc file, or setup and provide an API Key. Next, you must create a server_context, which is basically a meaningful way to fetch the data. Then, you must fetch the data with labkey.query.select_rows() Finally, you must use a filter on the data that you fetched, which you must either create ahead of time and access via a variable, or create dynamically within the labkey.query.select_rows() query--this method is shown below.*


        import labkey

        server_context = labkey.utils.create_server_context('dholk.primate.wisc.edu', 'dho/sequencing/Illumina', api_key='apikey|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', use_ssl=True)

        my_results = labkey.query.select_rows(
          server_context=server_context,
          schema_name='lists',
          query_name='miseqRuns',
          filter_array=[
            labkey.query.QueryFilter('notes', 'MiSeq', 'contains')
          ],
          sort='-run_num'
        )
        print(my_results)

* This can also be generated from the URL https://dholk.primate.wisc.edu/list/dho/sequencing/Illumina/grid.view?listId=1600 and selecting "Export" -> "Script"
  * Note that this option may only be available if you are an admin.

The data was manually formatted/parsed as a json, with the focus being to find an anchor keyword for searches. The general format that was used was:
* delete the top sections, they are descriptive headers
  * start at the entry "rows:" []
  * add a newline before each entry {"Operator":
    * *Comment from JC: The first rule of parsing data effectively is there is no set rule to parsing data effectively.  Here, I looked through the file for a commonly used keyword that I could use to divide the data up in a meaningful way. Any sharp-eyed observers that note this technique is very similar to tokenzing strings for Natural Language Processing gets a gold star.*
  * The above command will not alter a json file, i.e. newlines are still syntactically correct, but provide an additional anchor for parsing.
  * This will split all entries by row. Once newlines are added, the attached python script was used to parse out experiment ID, run ID, a timestamp, and to do an initial filter.
  * This narrowed the list to a manageable 174 entries.

Part II:
* Once a preliminary list of Experiment ID's was obtained, the following breadcrumb workflow was created.
  * Each experiment was examined for a suitable keyword to use for filtering (*Comment from JC: see my previous comment.*)
  * A test list was created, then validated against the list of MiSeq runs based on the number of experiments and similar matching.
    * *Comment from JC: An additional problem with this workflow is the experiments may not exactly match, hence describing this workflow as "breadcrumbs". For a more concrete and searchable example, if we search for a matching entry for the flagged MiSeq experiment 21249 from Part I, Experiment 21259, created by Roger, has a pivot table, matches Experiment 21249, and has the keyword "MiSeq140" as well as "CHOP1" in the notes. However, a closer look at these filtered results shows that Roger was the only one to reliably enter parent experiments, and the output from Part I clearly missed some of the outputs.*
  * Filter using the GUI or with a query for:
           SELECT *
           FROM experiments
           WHERE
               CreatedBy.DisplayName IS ONE OF ('gajewski', 'hbussan', 'namous', 'rwiseman')
               AND
               ExperimentType.DisplayName IS ONE OF ('MHC Genotyping Analysis' OR 'MHC Genotype Summary' OR 'MHC Genotyping analysis')

  * *Comment From JC*: Continuing from the previous comment, here we have a choice to make, and which we decide depends on what the final outcome will be.
    * There do not seem to be reliable patterns of descriptions in the notes, but keywords do exist.  Designing a parser that will act as a filter is doable, but difficult, and it would require a lot of time, effort, and a high degree of fine tuning and validation. This option would be useful if we wanted to be absolutely certain that all of a certain criteria were selected, or absolutely certain that none of a certain criteria were selected, but otherwise the effort is rarely worth the payout.
    * We could also simply pick one of the filters already described and use it. The risk is that we will probably include Type I errors (false positives, or incorrectly including results that are not MiSeq pivot tables), and we may include Type II errors (false negatives, or incorrectly excluding experiments with MiSeq pivot table results). For Type I errors, it means more work and not much else. For Type II errors, we hurt ourselves by discarding results when we don't need to, but it's possible that we may find discarded results when looking up experiments.  
  * Since we do not need to be absolutely certain that all MiSeq experiments are included, only reasonably certain, and there is no ambiguity in the final results, i.e. if a pivot table is present it is always the correct results, the second option is the route to go. Since the filter described in Part II both had more precise and more accurate results, that is the filter that will be used.  The output from Part I will be used as a secondary source of information, or to resolve uncertainty.
    * URL for this filter is [here](https://dholk.primate.wisc.edu/query/dho/experiments/executeQuery.view?schemaName=OConnorExperiments&query.queryName=Experiments&query.columns=ExperimentNumber%2CCreatedBy%2CCreated%2CModified%2CDescription%2CExperimentTypeId%2CGrantId%2CParentExperiments&query.CreatedBy/DisplayName~in=gajewski;hbussan;namous;rwiseman&query.Description~isnonblank=&query.ExperimentTypeId/Name~in=MHC%20Genotyping%20analysis;MHC%20Genotyping%20Analysis;MHC%20Genotype%20Summary)
    * python script for this is also attached
  * Manually parsed files, used the criteria: made by Roger Wiseman (traced experiment files to verify with reasonable accuracy that the pivot table from an experiment with multiple files was from Roger, not Hadjer or Ryan)
  * Stopped at 01/01/2018 and parsed out pivot tables as CSV to parse through pipeline, assess status of data
    * requirements are all Haplotypes have at least 2 (more is **much** better) replicated datapoints
  * Steps for AM:
  * use bash command below to create full allele list of ALL alleles:

          for i in *.csv ; do cat $i | cut -d, -f1 | cut -d_ -f2- | sort -n | uniq >> alleles_unparsed.txt ; done
          cat alleles_unparsed.txt | sort -n | uniq > alleles_parsed.txt

  * Then manually parse out files, including:
    * newlines at end of text files must be removed, this will cause an error
    * remove all quotation marks from the files, this will cause an error
    * remove all header entries from files, this will throw off the count
    * Finally, manually parse out MHC-A and MHC-B
    * Finally Finally, clean up this process and automate it
