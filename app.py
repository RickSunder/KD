from flask import Flask, render_template, url_for, request
import data
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/results", methods=['POST'])
def results():
    categories = get_category()
    appsizes = get_appsize()
    phone_brand = request.form.get("brand")
    operator = data.OperatorQuery(phone_brand)
    return render_template("results.html", categories = categories, appsizes = appsizes)

def get_category():
    categories = ['Games', 'Lifestyle','Music','Shopping','Entertainment']
    return [request.form[category] for category in categories if request.form.get(category)]

def get_appsize():
    appsizes = ["0to50MB","50to100MB","100to250MB","250to500MB",'500+MB']
    return [request.form[appsize] for appsize in appsizes if request.form.get(appsize)]

if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
