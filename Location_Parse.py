#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' A Verification tool to correct for a valid location'''


from spellchecker import SpellChecker
from stateAbbreviations import stateAbbr

# Returns combinations of a string input
def wordsCombination(county):
    candList = county.split(" ")
    combList = []
    
    # Taking all possible input of words in county (max 3 words) starting from end for most accuracy
    # Mainly used to erase extra unneeded words such as 'county'
    for indRange in range(len(candList),0,-1):
        stringCand = ""
        for indWord in range(indRange):
            if indWord ==indRange-1:
                stringCand += candList[indWord]
            else: 
                stringCand += candList[indWord] + " "
        combList.append(stringCand)
    return combList

# CandCounty is a string paramater that holds the desired location
# CandState should be abbreviated
def checkWordToLoc(candState, candCounty):
    f= open("us_cities_states_counties.txt")
    candCounty = candCounty.strip()
    lstOfCombinations = wordsCombination(candCounty)
    # For each candidate 
    for content in f:
        candLoc = content.split("|")
        if candLoc[1] == candState:
            for candComb in lstOfCombinations:
                if candLoc[3] == candComb:
                    print("Verified your location is ")
                    print(candState,candComb)
                    return (candLoc[1],candLoc[3])
        content = f.readline()
    f.close()
    return -1

# Checks if location input was correctly spelled
def locationSpellCheck(location):
    finalStr = ""
    
    # Each word in location
    for sep in location:
        spell = SpellChecker()
        misspelled = spell.unknown([sep])
        
        # If word is correctly spelled
        if len(misspelled) == 0:
            finalStr = finalStr + sep + " "
            
        # For each candidate in misspelled
        for word in misspelled:
            
            # Get the most likely answer
            candidateCorrection = spell.correction(word)
            
            # Get a list of likely options
            candidates = spell.candidates(word)
            
            # If no candidates were returned indicating an invalid word
            if len(candidates) == 1 and location == candidateCorrection:
                return -1
            else:
                finalStr = finalStr + candidateCorrection + " "
    return finalStr

# Takes abbreviated state name and returns full name
def abbrToName(abbr):
    for key,val in stateAbbr.items():
        if val == abbr:
            return key
    return -1

# Verifies the location accuracy for a specific input
def verifyLocation(stateCand,countyCand):
    countySeparated = countyCand.split(" ")
    countySpell = locationSpellCheck(countySeparated)
    finalVer = checkWordToLoc(stateCand.upper(), countySpell.upper())
    if finalVer == -1:
        print("Could not verify Location")
        return -1
    return finalVer
    
    
def main():
    print(verifyLocation("NY","Queensss"))
    print(wordsCombination("Fairfax"))
    
#main()