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
    size_limit = get_appsize()
    brands = get_brand()
    ages = get_ages()
    rating = get_rating()
    price = get_price()
    print(size_limit)
    #operator = data.OperatorQuery(brands)
    return render_template("results.html", categories = categories, appsizes = size_limit, brands = brands, ages = ages, rating = rating, price = price)


def get_category():
    categories = ['education', 'Entertainment', 'Finance', 'Games', 'Lifestyle & Helth', 
    'Music', 'Navigation & Travel', 'News & Sports', 'Photo & VIdeo', 'Reading', 
    'Shopping','Social Networking', 'Tools']
    return [request.form[category] for category in categories if request.form.get(category)]

def get_appsize():
    appsizes = ["0-50","50-100","100-250","250-500",'500-10000']
    size_request = [request.form[appsize] for appsize in appsizes if request.form.get(appsize)]
    if size_request:
        return size_request[0].split('-')
    else:
        return ['0', '10000']

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
