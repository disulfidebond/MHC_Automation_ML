#!/Users/thor/anaconda3/bin/python

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
