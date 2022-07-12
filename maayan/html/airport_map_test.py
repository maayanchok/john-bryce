from geopy.geocoders import Nominatim
import flights_table
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs

my_flights = (flights_table.flights_data)

def cities_set():
    
    my_cities = []
    for flight in my_flights:
        if flight["CHLOC1D"] != "":
           my_cities.append(flight["CHLOC1D"])
    my_cities = set(my_cities)
    return my_cities

my_cities = cities_set()

def get_loc(address):
    geolocator = Nominatim(user_agent="Maayan")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)


def get_list_loc(set_cities = set):
    cities_loc = []
    for city in set_cities:
        try:
            cities_loc.append(get_loc(city))
        except:
            continue
    return cities_loc
my_loc = get_list_loc(my_cities)  

x = []
y = []

for loc in my_loc:
    x.append(loc[0])
    y.append(loc[1])

xpoints = np.array(x)
ypoints = np.array(y)

ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

# Save the plot by calling plt.savefig() BEFORE plt.show()
plt.savefig('coastlines.pdf')
plt.savefig('coastlines.png')
plt.plot(x, y, marker='o',
         transform=ccrs.Geodetic(),
         )

plt.plot(xpoints, ypoints, 'o')
plt.show()