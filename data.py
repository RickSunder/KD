from SPARQLWrapper import SPARQLWrapper, JSON

def OperatorQuery(phone):
    """ Query dbpedia to check which operating system the users phone uses. 
        With this information, we know in which database to search for apps. 
        If a result comes out of this query, we know the device uses Android;
        otherwise it should be a device that uses IOS as operating system."""

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

print(OperatorQuery('ZTE'))