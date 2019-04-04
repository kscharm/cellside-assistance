from flask import Flask
from flask import render_template
import Database as Database

app = Flask(__name__)

@app.route('/')
def main():
    patientDb = Database.PatientCollection()
    print(patientDb.getPatient("3A3C2AFB-FFFA-4E69-B4E6-73C1245D5D12"))
    title =  "Cellside Assistance"
    phone = "(740)-872-0211"
    return render_template("index.html", title=title, phone=phone)

if __name__ == "__main__":
    app.run(debug=True)
