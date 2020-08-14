#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Takes input of user location and returns statistics by Country, State, and County'''

from StatsCollector import statsResponseCountry, statsResponseState, statsResponseCounty
from LocationParse import abbrToName, verifyLocation

def maximumWords(county):
    wordsInCounty = county.split(" ")
    if len(wordsInCounty) > 3 :
        shortenedStr = wordsInCounty[0] + " " + wordsInCounty[1] + " " + wordsInCounty[2]
        return shortenedStr
    return county
    
    
#country and state are abbreviated
def userLocToStats(country,state,county):
    county = maximumWords(county)
    countyVer = verifyLocation(state,county)
    if countyVer == -1:
        print("Location could not be verified or is not in the database yet, please look over your information and try again")
        return
    stateName = abbrToName(state)
    statsCountry = statsResponseCountry(country)
    statsState = statsResponseState(stateName)
    statsCounty = statsResponseCounty(stateName,countyVer[1])
    return (statsCountry,statsState,statsCounty)

def main():
    print(userLocToStats("US","VA","Fairfax County"))
    
main()
    