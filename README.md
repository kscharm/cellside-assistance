# Cellside Assistance
Helping remote medical personnel access critical patient information via SMS.

### Core Functionality
- /flask : Flask web application
  - Dockerfile : sets up Docker environment from scratch
  - Main.py : runs Flask web application on localhost
  - requirements.txt : list of dependencies to install in Docker environment
      - /static
        - Messenger.py : runs Google Voice server
        - Language.py : parses and formats reply message to user
        - Database.py : instantiates MongoDB connection and defines query operations
        - data.tsv : contains logging information of received and sent messages for security purposes
-  /patient-data
    - NamedPatientData.json : final dataset containing 10,000 fake patient documents
- /scripts : miscellaneous scripts used to manipulate and aggregate patient datasets

###  Dependencies
1. Python 3.5.X
2. GoogleVoice (PyPi) 
3. MongoDB
4. PyMongo
5. Flask
6. BS4 (BeautifulSoup 4)

### MongoDB Installation & Setup
1. [Install MongoDB](https://docs.mongodb.com/manual/administration/install-community) and choose the correct distribution (Linux, MacOS, Windows) of MongoDB Community Edition. Please follow the corresponding instructions for your distribution. The following instructions are for Windows hosts. 
2. Start the MongoDB service: ```net start MongoDB```
3. Verify that MongoDB has started successfully: ```[initandlisten] waiting for connections on port 27017```
4. Run the following to import the fake patient dataset: ```.\mongoimport.exe --db "cellsideAssistance" --collection "patients" --file "cellside-assistance\patient-data\NamedPatientData.json" --jsonArray```

### Google Voice Account Setup
1. [Create Google Voice Account](https://voice.google.com)
2. Choose a Google Voice number to link to your account
3. Store your account information in ```self.username``` and ```self.password``` in ```Messenger.py```

### Run Instructions
1. Navigate to ```\flask``` and run ```python Main.py``` to launch the Flask web application.
2. Navigate to ```\flask\static``` and run ```python Messenger.py``` to launch the Google Voice server.
3. Send text messages from your mobile phone to the Google Voice number you setup. Text the word ```help``` to get started!

### Docker Build Instructions
1. Enter the root directory of the project and run the following command to build the docker image for cellside. The first time this command is run, Docker will pull the latest sources and requirements. Therefore it will take a bit longer than normal as these sources are being cached.

```docker build -t cellside:latest .```

2. To run the image in a container with detached output, simpy run

```docker run -d -p 5000:5000 cellside```
