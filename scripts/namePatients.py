#!/usr/bin/env python

import csv
import json
import collections
import names

src1 = 'CombinedPatientData.json'
dst = 'NamedPatientData.json'
data = []

with open(src1) as f1:
    data1 = json.load(f1)
    for d1 in data1:
        named = d1
        if named["gender"] == "Male":
            named["name"] = names.get_full_name(gender='male')
        else:
            named["name"] = names.get_full_name(gender='female')
        data.append(named)

with open(dst, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=2)