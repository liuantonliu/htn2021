import json
import requests
import time
import urllib.parse

API_KEY = "AIzaSyCDheL3PDqX-t0V1O1W9YWFN7ygpdDH8bk"
#latitude, longitude
location = "43.47559912784776, -80.53574397301112"

#radius in meters
radius = 1000 
destination_type = "restaurant"
address = "280 Lester St., Waterloo, ON"

# Given an address, convert to lat/long
# returns a dictionary of {"lat": latidude, "lng": longitude}
def geocode_address(address):
    urllib.parse.quote(address)
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key="+API_KEY
    file = url_query(url)
    
    #only works with one return result for now, no error handling
    location = file["results"][0]["geometry"]["location"]

    return location

# given a url, return json file
def url_query(url):

    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)

    file = json.loads(response.text)
    
    return file

#returns list of nearby locations based on location (lat,lng), radius (m), destination type
def list_locations(location, radius, destination_type, API_KEY):
    next_page = True
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+location+"&radius="+str(radius)+"&type="+str(destination_type)+"&key="+API_KEY
    final_data = []
    while (next_page): 
        file = url_query(url)
        results = file["results"]
        final_data = final_data + results
        
        time.sleep(5)

        if 'next_page_token' in file:
            next_page_token = file['next_page_token']
            url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key='+str(API_KEY)+'&pagetoken='+str(next_page_token)
        else:
            next_page = False
    
    return final_data
