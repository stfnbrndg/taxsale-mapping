# Reads in tax sale properties CSV as data frame. Geocodes data using Google Maps API, then writes lat/long back to CSV in additional column.

import os
import pandas
import json
import requests
from datetime import datetime

# Add Googlemaps API key

for line in open('api_key.txt'):
    api_key = line
    print("Using API key " + api_key)

# // Read in addresses
csv = "taxsale.csv"

# Read addresses into dataframe
df = pandas.read_csv(csv, delimiter = ',', index_col=[0])

# Add latitude and longitude columns in dataframe
df['LATITUDE'] = "l"
df['LONGITUDE'] = "l"

# Get lat/long (geocode) each address in address column
addresses = df["PROP_ADDRESS"].tolist()

count = 0
for row in df.iterrows():
    url = "https://maps.googleapis.com/maps/api/geocode/json?address= %s &key= %s" % (addresses[count], api_key)
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    count += 1

# Print Address column contents without printing index column alongside
#addresses = df.to_string(columns=['PROP_ADDRESS'], index=False)
#addresses = df["PROP_ADDRESS"].tolist()
#print(addresses[2])


#with open('taxsale_clean.txt') as addresses:
#    for address in addresses:
#        address = address.rstrip('\n')
#        url = "https://maps.googleapis.com/maps/api/geocode/json?address= %s &key= %s" % (address, api_key)
#        print(url)
#        response = requests.get(url)
#        response_json = response.json()
#        print(response_json)
#        with open ('plotted_addresses.txt', 'w') as json:
#            json.dump(response.json, json)
