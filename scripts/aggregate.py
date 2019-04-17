#!/usr/bin/env python

import csv
import json
import collections

src1 = 'data.json'
src2 = 'data2.json'
dst = 'combined.json'
data = []

with open(src1) as f1:
    data1 = json.load(f1)
    with open(src2) as f2:
        data2 = json.load(f2)
        for d1 in data1:
            patientId = d1["patientId"]
            combined = d1
            combined["admissions"] = []
            for d2 in data2:
                if patientId == d2["patientId"]:
                    obj = {
                        "admissionId": d2["admissionId"],
                        "primaryDiagnosisCode": d2["primaryDiagnosisCode"],
                        "primaryDiagnosisDescription": d2["primaryDiagnosisDescription"]
                    }
                    combined["admissions"].append(obj)
            data.append(combined)

with open(dst, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=2)