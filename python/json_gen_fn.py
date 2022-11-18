import string as string
import random as random
from geopy.geocoders import Nominatim
import sys
import math

def rand_name():
    with open("./wordlists/names.txt", "r") as file:
        allText = file.read()
        name_list = list(map(str, allText.split()))
        name = random.choice(name_list)
    return name

def rand_user():
    with open("./wordlists/usernames.txt", "r") as file:
        allText = file.read()
        user_list = list(map(str, allText.split()))
        username = random.choice(user_list)
    return username

def gender():
    opt  = ["male", "female"]
    gender = random.choice(opt)
    return gender
    
lat = random.uniform(-29.77, 53.12)
lon = random.uniform(-29.77, 53.12)
num_rows = 1

def get_address(lati, longi):
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.reverse((lati, longi))

def generate_random_data(lat, lon, num_rows):
    for _ in range(num_rows):
        hex1 = '%012x' % random.randrange(16**12) # 12 char random string
        flt = float(random.randint(0,100))
        dec_lat = random.random()/100
        dec_lon = random.random()/100
        print('%s %.1f %.6f %.6f \n' % (hex1.lower(), flt, lon+dec_lon, lat+dec_lat))
        address = get_address((lat+dec_lat), (lon+dec_lon))
        return address
    
def get_address(lati, longi):
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.reverse((lati, longi))
    return location
        
