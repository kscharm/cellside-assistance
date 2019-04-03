from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    title =  "Cellside Assistance"
    phone = "(740)-872-0211"
    return render_template("index.html", title=title, phone=phone)

if __name__ == "__main__":
    app.run(debug=True)
