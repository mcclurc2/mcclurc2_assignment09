# Name:Chase McClure, Cameron Hogan, Riley
# email:mcclurc2@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: april 4 
# Course/Section: ADV APP DEV (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: this assignment is to see if we can construct a sql statment and get it to run in ecliple with having three other functions. our will to count how many coupons are free and then the third thing will print the function in a different class
# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this. this module taught us how to get eclipse to read a database sql code and to bring sql code from ssms
# Citations:canvas slides
# Anything else that's relevant: as of doing this no




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
    '''
    for park in parsed_json['data']:
        print (park)
    '''