import json
import requests
import time
import urllib.parse

API_KEY = "AIzaSyCDheL3PDqX-t0V1O1W9YWFN7ygpdDH8bk"
RADIUS = 10000
#latitude, longitude
location = "43.47559912784776, -80.53574397301112"
destination_type = "restaurant"
address = "280 Lester St., Waterloo, ON"

# Given an address, convert to lat/long
# returns a dictionary of {"lat": latidude, "lng": longitude}
def geocode_address(address, API_KEY=API_KEY):
    address = urllib.parse.quote(address)
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

def list_locations(location, destination_type, start_time, radius=RADIUS, API_KEY=API_KEY):
    final_data = []
    cleaned_data = []
    if destination_type == "restaurant":
        final_data = query_locations(location,destination_type, radius, API_KEY)
    else:
        final_data += query_locations(location, "activity", radius, API_KEY)
        final_data += query_locations(location, "shop", radius, API_KEY)
        final_data += query_locations(location, "tourist_attraction", radius, API_KEY)
    
    for result in final_data:
        end_location = "place_id:"+result["place_id"]
        temp = get_time(location, end_location,dept_time=start_time)
        clean = {"name": result["name"],
                "place_id": result["place_id"],
                "rating": result["rating"],
                "address": temp["destination_addresses"][0],
                "travel_time": temp["rows"][0]["elements"][0]["duration"]["value"]
        }
        cleaned_data.append(clean)


    return cleaned_data

#returns list of nearby locations based on location (lat,lng), radius (m), destination type
def query_locations(location, destination_type, radius=RADIUS, API_KEY=API_KEY):
    location = geocode_address(location)
    location = str(location["lat"])+", "+str(location["lng"])
    next_page = True
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+location+"&radius="+str(radius)+"&keyword="+str(destination_type)+"&key="+API_KEY
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

def get_time(start_loc, end_loc, mode="DRIVING", dept_time="now", API_KEY=API_KEY):
    """
    Get good. Get travel times.

    start_loc: str
        Full starting address in a string seperated by commas. e.g. 280 Lester St., Waterloo, ON
    end_loc: str
        Full destination address in a string seperated by commas. e.g. 280 Lester St., Waterloo, ON
    mode: str
        Method of transportation. See https://developers.google.com/maps/documentation/distance-matrix/overview#mode for list of supported modes.
    dept_time: str
        dictionary containing coordiates of end location in the following format. Keys must be the same.
        e.g. {'lat': 43.4756084, 'lng': -80.53572779999999}

    returns : None
    """
    start_loc = urllib.parse.quote(start_loc)
    if "place_id:" not in end_loc:
        end_loc = urllib.parse.quote(end_loc)

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+start_loc+"&destinations="+end_loc+"&departure_time="+dept_time+"&mode="+mode+"&key="+API_KEY
    file = url_query(url)
    return file