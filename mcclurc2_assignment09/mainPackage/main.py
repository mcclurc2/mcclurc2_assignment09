# Name:Chase McClure, Cameron Hogan, Riley
# email:mcclurc2@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: april 4 
# Course/Section: ADV APP DEV (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: this assignment is to see if we can get an api url and to read informatoin. to take the url run code to read and get important informaiation from it as well to be able to follow directions and do what the assignment says
# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this. this module shows us how to connect to an api from eclipse and to read it rfom here
# Citations:canvas slides
# Anything else that's relevant: as of doing this no


#https://secure.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=9&alpha=c&page=1

from functionPackage.runescapeClass import *
#main.py

if __name__ =="__main__":
    results = extractInfo()
    print(results)
