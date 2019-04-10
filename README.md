# Cellside Assistance
Helping remote medical personnel access critical patient information via SMS.

###  Dependencies
1. Python 3.5.X
2. GoogleVoice (PyPi) 
3. MongoDB
4. Virtualenv

### Tasks
- Frontend
    - [ ] asyn loading
    - [ ] clear button/show only 10 items
    - [?] possibly verified numbers list display
- [X] Dockerize Everything
- [X] natural langugage processing using key values (nltk)
- [ ]Clean up reponses


### Mongo
`mongoimport --host localhost:27017 --db patientDatabase --collection patients ./patient-data/NamedPatientData.json  --jsonArray`
