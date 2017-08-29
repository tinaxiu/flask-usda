from urllib.request import urlopen
from urllib.parse import quote_plus
import pandas as pd
import json
import matplotlib
matplotlib.use('Agg')

Keys = "Z7P0l57jXrxJ0naBSGCcChUSs3DqTXF36BlrsvVq"

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def fetch_url(url):
    urlHandler = urlopen(url)
    return urlHandler.read().decode('utf-8')

def nutrientFromdbno(dbno):
    base = "https://api.nal.usda.gov/ndb/reports/?ndbno="
    more = "&type=f&format=json&api_key="
    url = base + dbno + more + Keys
    data = json.loads(fetch_url(url))

    data = pd.DataFrame.from_dict(data["report"]["food"]["nutrients"])
    data = data.loc[:,["group","name","unit","value"]]
    return data

def GetNutrienlist(query):
    query = quote_plus(query.lower())
    url = "https://api.nal.usda.gov/ndb/search/?format=xml&q=" + query + "&max=10&offset=0&api_key=" + Keys
    data = fetch_url(url)
    root = ET.fromstring(data)

    dbno = [list(root)[i].find('ndbno').text for i in range(len(list(root)))]
    dbname = [list(root)[i].find('name').text for i in range(len(list(root)))]
    dblist = {'id': dbno,
              'name': dbname}




#    data = pd.DataFrame(columns=['group','name','unit'])

#    for no in dbno:
#        datum = nutrientFromdbno(no)
#        print(datum)
#        data = data.merge( datum, on=['group','name','unit'],how='outer')
    print(dblist)
    return dblist