# Cellside Assistance
Helping remote medical personnel access critical patient information via SMS.

###  Dependencies
1. Python 3.5.X
2. GoogleVoice (PyPi) 
3. MongoDB
4. PyMongo
5. Flask
6. BS4

### MongoDB Installation & Setup

1. [Install MongoDB](https://docs.mongodb.com/manual/administration/install-community) and choose the correct distribution (Linux, MacOS, Windows) of MongoDB Community Edition. Please follow the corresponding instructions for your distribution. The following instructions are for Windows hosts. 
2. Start the MongoDB service: ```net start MongoDB```
3. Verify that MongoDB has started successfully: ```[initandlisten] waiting for connections on port 27017```
4. Run the following to import the fake patient dataset: ```.\mongoimport.exe --db "cellsideAssistance" --collection "patients" --file "cellside-assistance\patient-data\NamedPatientData.json" --jsonArray```

### Tasks
- Frontend
    - asyn loading
    - show only 10 items
    - (possible) verified numbers list display
    - column headers
- Dockerize everything
- Clean up reponses
