from SPARQLWrapper import SPARQLWrapper, JSON
import urllib.parse
import app

def OperatorQuery(phone):
    """ Query dbpedia to check which operating system the users phone uses. 
        With this information, we know in which database to search for apps. 
        If a result comes out of this query, we know the device uses Android;
        otherwise it should be a device that uses IOS as operating system."""

    if phone == 'Other':
        """ If the user has another Android phone than listed on the html page, the query
        won't always work because of the range of dbpedia's database and different namings etc.
        Therefore we display a button on the html page that's for other Android phones than listed;
        these phones naturally run on Android."""
        return 'Android'
    
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    
    sparql.setQuery("""
        PREFIX dct: <http://purl.org/dc/terms/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT *
        WHERE {
        ?phone dbo:manufacturer dbr:%s . 
        ?phone dbo:operatingSystem ?operator .
        ?operator dct:subject <http://dbpedia.org/resource/Category:Android_(operating_system)>
        }
    """%phone) 
    
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    results = [result["operator"]["value"] for result in results["results"]["bindings"]]
    if results:
        return 'Android'
    else:
        return 'IOS'

def results_query(operator, category, size, rating, age, price):
    """ Query our own ontology in our local GraphDB SPARQL endpoint. The query depends 
        on what the user wants the application to filter. If the user doesn't particularly 
        filters on an aspect, this won't be filled in in the query.
        
        Because the instances are bound to our prefix, the spaces and special characters have been 
        replaced with URL-characters, like %20 and %26. Therefore, the results are mutated to normal
        characters, like a space or the &-sign. The characteristics of every mobile app are declared 
        in a dictionairy. Every dictionairy represents an mobile application."""

    if operator == 'Android':
        operator_query = '?app a pr:AndroidApp .'
    elif operator == 'Apple':
        operator_query = '?app a pr:AppleApp .'
    else:
        operator_query = ''
    
    if type(category) == str:
        category_query = '?app a pr:%s .'%category
    else:
        category_query = ''

    if age:
        age_query = '?app a pr:%s .'%age
    else:
        age_query = ''

    if price == 'Free':
        price_query = '?app a odapp:FreeApp .'
    else:
        price_query = ''

    query_variables = (operator_query, category_query, size[0], size[1], rating, age_query, price_query)

    sparql = SPARQLWrapper("http://localhost:7200/repositories/KaDPROJECT")

    sparql.setQuery("""
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX pr: <http://www.project2.nl/>
        PREFIX odapp: <http://vocab.deri.ie/odapp#>
        
        SELECT *
        WHERE {
            %s
            %s
            ?app pr:hasSize ?size
            FILTER(?size >= %s && ?size <= %s)
            ?app pr:hasUserRating ?userrating
            FILTER(?userrating >= %s)
            %s
            %s 
            ?app pr:hasName ?name .
            ?app pr:hasPrice ?price .
            ?app pr:hasNumberOfRatings ?numb_ratings .
            ?app pr:hasCurrency ?currency .
        }
    """%query_variables)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    app_list = []
    for result in results["results"]["bindings"]:
        app_list.append({'name' : urllib.parse.unquote(result['name']['value'][23:]), 'currency' : urllib.parse.unquote(result['currency']['value'][23:]), 'price' : urllib.parse.unquote(result['price']['value'][23:]),
         'size' : urllib.parse.unquote(result['size']['value']), 'user_rating' : urllib.parse.unquote(result['userrating']['value']), 
         'numb_ratings' : urllib.parse.unquote(result['numb_ratings']['value'])})
    
    return app_list