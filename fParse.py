#!/Users/thor/anaconda3/bin/python

import re

l = []
with open('labKeyResults.txt', 'r') as f:
    for i in f:
        i = i.rstrip('\r\n')
        l.append(i)

for i in l:
    iSplit = i.split(',')
    parsedEntryString = ''
    parsedEntryDate = ''
    parsedEntryExperimentID = ''
    parsedEntryRunID = ''
    for itmKey in iSplit:
        if 'notes' in itmKey:
            parsedEntry = itmKey[9:]
            m = re.search('MiSeq\d+', parsedEntry)
            if m:
                parsedEntryString = parsedEntry
                parsedEntryString = parsedEntryString.replace('"', '')
        if 'Created"' in itmKey:
            parsedEntry = itmKey[12:]
            parsedEntry = parsedEntry.replace('"', '')
            parsedEntryDate = parsedEntry
        if 'exp_num' in itmKey:
            parsedEntry = itmKey[11:]
            parsedEntryExperimentID = parsedEntry
        if 'run_num' in itmKey:
            parsedEntry = itmKey[11:]
            parsedEntryRunID = parsedEntry
    if parsedEntryString:
        print('MatchedEntry: ' + str(parsedEntryString))
        print('MatchedEntryDate: ' + str(parsedEntryDate))
        print('MatchedEntryExpID: ' + str(parsedEntryExperimentID))
        print('MatchedEntryRunID: ' + str(parsedEntryRunID))
        print('####\n\n')
