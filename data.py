from SPARQLWrapper import SPARQLWrapper, JSON
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






def OperatorQuery(phone):

    if phone == 'Other':
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


