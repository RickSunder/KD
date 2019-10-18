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
    return render_template("results.html", categories = categories)

def get_category():
    checked_categories = []
    categories = ['Games', 'Lifestyle','Music','Shopping','Entertainment']
    for category in categories:
        if request.form.get(category):
            checked_categories.append(request.form[category])
    return checked_categories

def get_category():
    checked_categories = []
    categories = ['Games', 'Lifestyle','Music','Shopping','Entertainment']
    for category in categories:
        if request.form.get(category):
            checked_categories.append(request.form[category])
    return checked_categories


if __name__ == "__main__":
    app.run(debug=True)
