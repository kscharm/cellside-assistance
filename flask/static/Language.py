import Database

class Language():
    def __init__(self):
        self.patientDatabase = Database.PatientCollection()

    def reply(self, text):
        return self.patientDatabase.getPatient(text)
        
    def format(self, obj):
        separator = "\t"
        if obj == None:
            reply = "Error, please provide a valid Patient ID."
        else:
            reply = ''
            for key, val in obj.items():
                if type(val) is str:
                    reply += str(key) + ": " + str(val)  + separator
                if type(val) is list:
                    admissions = ''
                    for admission in val:
                        admissions += 'code: ' + admission["primaryDiagnosisCode"] + ' ' + admission["primaryDiagnosisDescription"] + separator
            reply += admissions
        return reply