# -*- coding: utf-8 -*-

''''Reports Statistics for specified locations'''

import requests
from stats.LocationParse import abbrToName, verifyLocation

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
    stateName = abbrToName(state)
    page = "https://corona.lmao.ninja/v2/states/" + stateName + "?yesterday=false"
    response = requests.get(page)
    convJSON = response.json()
    '''
    newDict = {
        "state": convJSON['state'],
        "cases": convJSON['cases'],
        "todayRecovered": convJSON["todayRecovered"],
        "recovered": convJSON['recovered'],
        "todayDeaths": convJSON['todayDeaths'],
        "deaths": convJSON['deaths']
    }
    '''
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
    newDict = {
        "country": convJSON['country'],
        "todayCases": convJSON['todayCases'],
        "cases": convJSON['cases'],
        "todayRecovered": convJSON["todayRecovered"],
        "recovered": convJSON['recovered'],
        "todayDeaths": convJSON['todayDeaths'],
        "deaths": convJSON['deaths']
    }
    return newDict

def main():
    country = "US"
    state = "New York"
    county = "Nassau"
    print(statsResponseCounty(state,county))
    print(statsResponseCountry("Trinidad and Tobago"))
    print(statsResponseState(state))

#main()