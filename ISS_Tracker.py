# Tyler Norman
# Requires requests and cartopy (from conda environment)

import requests
from datetime import datetime
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import time

loc = requests.get('http://api.open-notify.org/iss-now.json')   # Get .json files from NASA public API
people = requests.get('http://api.open-notify.org/astros.json')

if loc.status_code != 200 or people.status_code != 200: # Checks if API is available
    print('Error getting API')
    quit()


loc_json = loc.json()       # Convert from json to Python
people_json = people.json()

print("There are", people_json['number'], "people in space right now.")

if people_json['number'] > 0:   # Display current astronauts
    for i in people_json['people']:
        print(i['name'].ljust(20, " "), " currently onboard", i['craft'])

print("\nThe ISS coordinates as of", datetime.fromtimestamp(loc_json['timestamp'])) # Display first read of a date timestamp
print("LATITUDE: ", loc_json['iss_position']['latitude'], "\nLONGITUDE:", loc_json['iss_position']['longitude'], '\n')

while 1 < 2: # inf

    ax = plt.axes(projection=ccrs.PlateCarree()) # Plot world map
    ax.stock_img()

    loc = requests.get('http://api.open-notify.org/iss-now.json')
    loc_json = loc.json()
    
    lat = float(loc_json['iss_position']['latitude'])
    lon = float(loc_json['iss_position']['longitude'])
    
    plt.plot(lon, lat, color='blue', linewidth=2, marker='o', transform=ccrs.PlateCarree())     # Plot location of ISS
    plt.text(lon - 3, lat - 10, 'ISS', horizontalalignment='right', transform=ccrs.Geodetic())
    plt.pause(5)    # Pause 5 seconds
    plt.clf()       # Clear previous position
