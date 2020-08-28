#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:01:14 2020

@author: mikesingh
"""
import requests

def main():
    file = open("AvailableCountries.txt",'w')
    page = "https://corona.lmao.ninja/v2/countries"
    response = requests.get(page)
    convJSON = response.json()
    file.write('<select name = country> \n')
    for entry in convJSON:
        file.write('\t')
        file.write('<option')
        file.write(" value = '" + entry['country'] + "'>")
        file.write(entry['country'])
        file.write('</option>')
        file.write('\n')
    file.write('</select> \n')
    return

main()