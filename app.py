from flask import Flask, render_template, url_for, request
import data
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/results", methods=['POST'])
def results():
    ''' getting the information given from the user '''
    categories = get_category()
    size_limit = get_appsize()
    brand = get_brand()
    ages = get_ages()
    rating = get_rating()
    price = get_price()
    operator = data.OperatorQuery(brand)
    
    print(data.results_query(operator, categories, size_limit, rating, ages, price))
    return render_template("results.html", categories = categories, appsizes = size_limit, brands = brand, ages = ages, rating = rating, price = price)


def get_category():
    categories = ['Education', 'Entertainment', 'Finance', 'Games', 'Lifestyle & Health', 
    'Music', 'Navigation & Travel', 'News & Sports', 'Photo & VIdeo', 'Reading', 
    'Shopping','Social Networking', 'Tools']
    if request.form.get('category'):
        category = request.form['category']
        
        return category
    else:
        return categories

def get_appsize():
    appsizes = ["0-50","50-100","100-250","250-500",'500-10000']
    size_request = [request.form[appsize] for appsize in appsizes if request.form.get(appsize)]
    if size_request:
        return size_request[0].split('-')
    else:
        return ['0', '10000']

def get_ages():
    ages = request.form.get('age')
    return ages

def get_rating():
    rating = request.form.get('rating')
    if not rating:
        rating = 1
    return rating

def get_brand():
    return request.form.get('brand')

def get_price():
    price = request.form.get('price')
    if not price:
        price = 'Irrelevant'
    return price

if __name__ == "__main__":
    app.run(debug=True)
