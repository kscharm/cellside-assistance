import Database
import re

class Language():
    def __init__(self):
        self.patientDatabase = Database.PatientCollection()

    def reply(self, text):
        isName = bool(re.match('[A-z]{2,25}( [A-z]{2,25}){1}', text))
        isPatientId = bool(re.match('[A-z0-9]{8}-[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{12}', text))
        isHelp = bool("help" in text.lower())
        fields = ["maritalStatus", "name", "language", "gender", "patientId", "admissions", "dateOfBirth", "race", "populationPercentageBelowPoverty"]
        hashTag = "#" in text
        if isHelp:
            return "help"
        elif isName or isPatientId:
            if hashTag:
                startIndex = text.index("#") + 1
                field = text[startIndex : len(text)]
                if field not in fields:
                    return None
                if isName:
                    match = re.search('[A-z]{2,25}( [A-z]{2,25}){1}', text)
                    name = match.group(0)
                    return self.patientDatabase.getPatientByNameSpecific(name, field)
                else:
                    match = re.search('[A-z0-9]{8}-[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{12}', text)
                    patientId = match.group(0)
                    return self.patientDatabase.getPatientByIdSpecific(patientId, field)
            else:
                if isName:
                    match = re.search('[A-z]{2,25}( [A-z]{2,25}){1}', text)
                    name = match.group(0)
                    return self.patientDatabase.getPatientByName(name)
                else:
                    match = re.search('[A-z0-9]{8}-[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{4}-[A-z0-9]{12}', text)
                    patientId = match.group(0)
                    return self.patientDatabase.getPatientById(patientId)
        else:
            return None
        
    def format(self, obj):
        separator = "\t"
        print(obj)
        if obj is None:
            reply = "Invalid request. For more help, please text the word 'help'."
        elif obj == "help":
            reply = ("Welcome to Cellside Assistance! "
                    "To access patient records, send one of the following: "
                    "'<PATIENT NAME> or <PATIENT_ID>. "
                    "To query specific information about a patient, "
                    "use the # symbol followed by the field name.\n"
                    "Ex. Kenny Scharm #admissions")
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