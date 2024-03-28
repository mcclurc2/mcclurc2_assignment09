#main.py
import requests
import json
#https://secure.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=9&alpha=c&page=1

if __name__ =="__main__":
    response = requests.get('https://secure.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=9&alpha=c&page=1')
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    print(parsed_json)
    #print(parsed_json['data'][0]['description'])
    #print(parsed_json['data'][0]['directionsInfo'])
    
    total = int(parsed_json['total']) # The number of parks that were returned
    
    for park in parsed_json['data']:
        print (park)