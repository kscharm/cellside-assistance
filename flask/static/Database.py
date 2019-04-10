from pymongo import MongoClient
from bson import ObjectId
import json

host = 'localhost'
port = 27017
dbName = 'cellsideAssistance'

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

    def getPatientById(self, patientId):
       return self.collection.find_one({'patientId': patientId})

    def getPatientByIdSpecific(self, patientId, field):
       return self.collection.find_one({'patientId': patientId}, { field : 1, '_id': 0 })
    
    def getPatientByName(self, name):
        return self.collection.find_one({'name': name})

    def getPatientByNameSpecific(self, name, field):
        return self.collection.find_one({'name': name}, { field : 1, '_id': 0 })

    def updatePatient(self, patientId, patient):
        return self.collection.update_one({'id': patientId}, patient)

    def deletePatient(self, patiendId):
        return self.collection.delete_one({'id': patientId})
    
    def createPatient(self, patient):
        return self.collection.insert(patient)