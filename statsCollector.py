# -*- coding: utf-8 -*-

''''Reports Statistics for specified locations'''

import requests

# Defines statistics for a specific county
# Requires full name of state and county (abbreviations will not work)
# If this function returns -1 then the state isn't correct or 
# state + county combination couldnt be found
def statsResponseCounty(state,county):
    page = "https://corona.lmao.ninja/v2/jhucsse/counties/" + county
    response = requests.get(page)
    convJSON = response.json()
    countyStats = -1 
    
    # For each province with the same name, confirm the correct state
    for entry in convJSON:
        if entry["province"] == state:
            countyStats = entry["stats"] 
        else:
            continue
    return countyStats

#defines statistics for a specific state
#Requires full name of state (abbreviations will not work)
def statsResponseState(state):
    page = "https://corona.lmao.ninja/v2/states/" + state + "?yesterday=false"
    response = requests.get(page)
    convJSON = response.json()
    return convJSON

#defines statistics for a specific country
#Can use either abbreviation or country name
def statsResponseCountry(country):
    page = "https://corona.lmao.ninja/v2/countries/" + country + "?yesterday=true&strict=true&query"
    response = requests.get(page)
    convJSON = response.json()
    #"message" is a default error message for an invalid country
    if "message" in convJSON:
        return convJSON["message"]
    return convJSON

def main():
    country = "US"
    state = "New York"
    county = "Nassau"
    #print(statsResponseCounty(state,county))
    #print(statsResponseCountry(country))
    #print(statsResponseState(state))

#main()