#!/usr/bin/env python

import csv
import json
import collections

# aliases
OrderedDict = collections.OrderedDict

src = 'PatientCorePopulatedTable.txt'
dst = 'data.json'
header = [
    "patientId", "gender","dateOfBirth", "race", "maritalStatus", "language", "populationPercentageBelowPoverty"
]

data = []
with open(src, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
    firstRow = True
    for row in reader:
        if firstRow:
            firstRow = False
            continue
        row = filter(None, row)
        data.append(OrderedDict(zip(header, row)))

with open(dst, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=2)