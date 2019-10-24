from flask import Flask, render_template, url_for, request
import data
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/results", methods=['POST'])
def results():
    #getting the information given from the user
    categories = get_category()
    appsizes = get_appsize()
    brands = get_brand()
    ages = get_ages()
    rating = get_rating()
    price = get_price()

    #operator = data.OperatorQuery(brands)
    return render_template("results.html", categories = categories, appsizes = appsizes, brands = brands, ages = ages, rating = rating, price = price)


def get_category():
    categories = ['education', 'Entertainment', 'Finance', 'Games', 'Lifestyle & Helth', 
    'Music', 'Navigation & Travel', 'News & Sports', 'Photo & VIdeo', 'Reading', 
    'Shopping','Social Networking', 'Tools']
    if request.form.get('category'):
        category = request.form['category']
        
        return category
    else:
        return categories

def get_appsize():
    appsizes = ["0to50MB","50to100MB","100to250MB","250to500MB",'500+MB']
    return [request.form[appsize] for appsize in appsizes if request.form.get(appsize)]

def get_ages():
    ages = ["Kids(-12)","Teens(12-18)","Adults(18+)"]
    return [request.form[age] for age in ages if request.form.get(age)]

def get_rating():
    return [request.form[rating] for rating in range(1,6) if request.form.get(rating)]

def get_brand():
    brands = ["Apple", "Samsung", "Huawei", "Xiaomi", "Other"]
    return [request.form[brand] for brand in brands if request.form.get(brand)]

def get_price():
    return [request.form[price] for price in ["Paid", "Free"] if request.form.get(price)]


if __name__ == "__main__":
    app.run(debug=True)
