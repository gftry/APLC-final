from Exceptions import invalidspoterror, parkingfullerror
import json
from json import dumps

file_path = 'APLC final\sampledata.json'

# load json file
try:
    with open(file_path, 'r') as data:
        data_dict = json.load(data)

except FileNotFoundError:
    print(f"File {file_path} doesn't exist")

# parse data to find available spots for each vehicle
for vehicle in data_dict['vehicles']:
    parked = False

    for spot in data_dict['parkingSpots']:
        if spot['available'] and vehicle['size'] == spot['size']:
            
            print(f"Spot {spot['id']} is available for {vehicle['plate']}")
            
            spot['available'] = False  
            parked = True
            break

    if not parked:
        print(f"No available spot for vehicle {vehicle['plate']}")
