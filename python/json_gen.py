import json
from json_gen_fn import *

user_infos = {
    
        "name": rand_name(),
        "username": rand_user(),
        "email": "marcellaharrell@frolix.com",
        "gender": gender(),
        "person_id": 121,
        "birthdate": "2012-3-10",
        "documents": [
          {
            "doctype": "CPF",
            "rand_cpfnumber": 40632376748
          }
        ],
        "address": [
          {
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
                "phone_number": "96 4 542748543",
                "type": "cellphone"
              }
            ]
          }
        ]
      }
my_json = json.dumps(user_infos, indent=2)
with open("json/sample.json", "w") as outfile:
    outfile.write(my_json)
print(my_json)