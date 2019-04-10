from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    title =  "Cellside Assistance"
    phone = "(740)-872-0211"
    return render_template("index.html", title=title, phone=phone)

@app.route('/clearTable')
def clearTable():
    open("./static/data.tsv", 'w').close()
    return ('', 204)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
