from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/results")
def results():
    return render_template("results.html")

# app.route()
# def getvalues():
#     category =request.form[]


if __name__ == "__main__":
    app.run(debug=True)
