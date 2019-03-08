from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from bson import ObjectId
import json

host = 'cloud.tlee753.com'
port = 32768
dbName = 'patientDatabase'


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class MongoConnection(object):
    def __init__(self):
        client = MongoClient(host, port)
        self.db = client[dbName]

    def get_collection(self, name):
        self.collection = self.db[name]

class PatientCollection(MongoConnection):
    def __init__(self):
       super(PatientCollection, self).__init__()
       self.get_collection('patients')

    def getPatient(self, patientId):
       return self.collection.find_one({'patientId': patientId})

    def updatePatient(self, patient):
        # TODO: update patient info
        return self.collection.find_one({'id': patient.patientId})


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def home(request):
    patientDB = PatientCollection()
    patient = patientDB.getPatient("3A3C2AFB-FFFA-4E69-B4E6-73C1245D5D12")
    return HttpResponse(JSONEncoder().encode(patient))