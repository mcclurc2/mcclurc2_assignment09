import requests

import json

 

class runescape:

    '''

   runescape class

    this class makes calls to runescape API to extract important information

    '''

 

def extractInfo():

 

    response = requests.get('https://secure.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=9&alpha=c&page=1')

    json_string = response.content

   

    parsed_json = json.loads(json_string) # Now we have a python dictionary