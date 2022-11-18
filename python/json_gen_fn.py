import string as string
import random as random
from geopy.geocoders import Nominatim
from cpf_generator import CPF
def rand_name():
    with open("wordlists/names.txt", "r") as file:
        allText = file.read()
        name_list = list(map(str, allText.split()))
        name = random.choice(name_list)
        surname = random.choice(name_list)
    return name + " " + surname

def rand_user():
    with open("wordlists/usernames.txt", "r") as file:
        allText = file.read()
        user_list = list(map(str, allText.split()))
        username = random.choice(user_list)
    return username

def gender():
    opt  = ["male", "female"]
    gender = random.choice(opt)
    return gender

n1 = -29.77 
n2 = 53.12
lat = random.uniform(n1, n2)
lon = random.uniform(n1, n2)
num_rows = 1

def get_lat(lat):
    dec_lat = random.random()/100
    return lat+dec_lat

def get_lon(lon):
    dec_lon = random.random()/100
    return lon+dec_lon
        
def generate_random_data(latitude, longitude):
    print('%.6f %.6f \n' % (longitude, latitude))
    address = get_address((latitude), (longitude))
    if address == None:
        late = random.uniform(n1, n2)
        longe = random.uniform(n1, n2)
        generate_random_data(late, longe)
    return str(address)
    
def get_address(lati, longi):
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.reverse((lati, longi))
    print(location)
    return location

def rand_email():
    return rand_user() + "@fakemail.com"

def birthday():
    return  str(random.randint(1960, 2005)) + "-" + str(random.randint(1, 12)) + "-" + str(random.randint(1, 28))

def cpf_gen():
    return CPF.generate()

def cellphone():
    country = str(random.randint(1, 200))
    if country != 55:
        return "+" + country + " " + str(random.randint(111111111, 999999999))
    return "+" + country + " " + str(random.randint(41, 55)) + " " + str(random.randint(111111111, 999999999)) # Se for BR acrescenta o DDD