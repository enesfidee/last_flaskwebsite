from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    pass
    return render_template("index.html")

@app.route("/home")
def home():
    pass
    return render_template("home.html")

@app.route("/home/en")
def home_en():
    pass
    return render_template("home_en.html")

if __name__ =="__main__":
    app.run(debug=True)