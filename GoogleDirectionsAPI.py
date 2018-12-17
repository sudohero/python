# simple use of the Directions API from Google Maps

import requests
import json

# set the starting piece of the directions request
request_start = 'https://maps.googleapis.com/maps/api/directions/json?'

# set the variables to load my API key from a json file
# prompt the user for the starting point, destination
# setup remaining piece of the request url
api_key = json.loads(open('apikey.json').read())
origin = input('Starting Point:\n').replace(' ','+')
destination = input('Destination:\n').replace(' ','+')
nav_request = f'origin={origin}&destination={destination}&key={api_key[0]}'

# put the complete request url together
full_req = request_start + nav_request

# get the request data and dump it into a json file
response = requests.get(full_req)
directions = json.loads(response.text)

# setup variables to display to the user by querying new json file
start_addr = directions['routes'][0]['legs'][0].get('start_address')
end_addr = directions['routes'][0]['legs'][0].get('end_address')
distance = directions['routes'][0]['legs'][0]['distance'].get('text')
duration = directions['routes'][0]['legs'][0]['duration'].get('text')
steps = directions['routes'][0]['legs'][0]['steps']

# once the user has entered the start point and dest, display directions
print(f"Directions from {start_addr} to {end_addr}:\n\n" \
      f"Distance: {distance}\n" \
      f"Time: {duration}\n\n" \
      "Route Information: \n")

# loop through the route info and display to user including time
# and distance for each step of the route
for i in range(len(steps)):
    print(f"+  {steps[i].get('html_instructions')}")
    print(f"\t->Travel {steps[i]['distance'].get('text')} for {steps[i]['duration'].get('text')}")
