# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

query = """SELECT ?company ?companyLabel ?industryLabel ?productOrServiceLabel ?founderLabel ?revenue
WHERE
{
  # Find Microsoft entities
  ?company wdt:P31 wd:Q4830453.  # Must be an instance of "business enterprise"
  ?company rdfs:label ?label.
  FILTER(LCASE(?label) = "microsoft"@en).
  OPTIONAL { ?company wdt:P452 ?industry. }  # Industry classification
  OPTIONAL { ?company wdt:P1424 ?productOrService. }  # Notable product or service
  OPTIONAL { ?company wdt:P1122 ?founder. }  # Founder(s)
  OPTIONAL { ?company wdt:P2139 ?revenue. }  # Revenue
  BIND(IRI(CONCAT("https://en.wikipedia.org/wiki/", REPLACE(STR(?company), ".*Q", ""))) AS ?wikipediaURL)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
LIMIT 10

"""


def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)
print(results)
print("------")
for result in results["results"]["bindings"]:
    print(result)
