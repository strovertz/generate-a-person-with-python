import json
from json_gen_fn import *

user_infos = {
    
        "name": rand_name(),
        "username": rand_user(),
        "email": rand_email(),
        "gender": gender(),
        "person_id": 121,
        "birthdate": birthday(),
        "documents": [
          {
            "doctype": "CPF",
            "rand_cpfnumber": cpf_gen()
          }
        ],
        "address": [
          {
            "GeoLoc": generate_random_data(get_lat(lat), get_lon(lon)),
            "city": "Williamsburg Street",
            "address_number": 257,
            "country_residence": "Saint Lucia",
            "province": "Virginia",
            "street": "Laurelton",
            "zip": 26492
          }
        ],
        "contacts": [
          {
            "phones": [
              {
                "phone_number": cellphone(),
                "type": "cellphone"
              }
            ]
          }
        ]
      }

my_json = json.dumps(user_infos, indent=2)
with open("json/user_data.json", "w") as outfile:
    outfile.write(my_json)
print(my_json)
