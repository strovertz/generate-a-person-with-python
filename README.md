﻿# Generate a Person With Python


## Objetivo

Gerar dados pessoais ficticios para auxiliar devs a testarem suas ferramentas, o código gera um Json contendo email, nome, sobrenome, data de nascimento, fone, cpf, etc.

## Funcionamento
Gera dados aleatórios e coleta nomes de forma randomica de wordlists. O output traz diferentes informações pessoais de uma pessoa fictícia, o CPF é gerado utilizando a biblioteca cpf_generator, pois dessa forma atende ao algoritmo de definição de CPF.

## Output

```JSON
[
      {
        "name": "Alisa Harrell",
        "username": "Marcella",
        "email": "marcellaharrell@frolix.com",
        "gender": "female",
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
      },
      {
        "name": "Good Davenport",
        "username": "Ramsey",
        "email": "ramseydavenport@frolix.com",
        "gender": "male",
        "person_id": 121,
        "birthdate": "2015-8-15",
        "documents": [
          {
            "doctype": "CPF",
            "rand_cpfnumber": 82334668289
          }
        ],
        "address": [
          {
            "city": "Sutter Avenue",
            "address_number": 651,
            "country_residence": "Puerto Rico",
            "province": "Florida",
            "street": "Volta",
            "zip": 92537
          }
        ],
        "contacts": [
          {
            "phones": [
              {
                "phone_number": "94 6 952812898",
                "type": "cellphone"
              }
            ]
          }
        ]
      }
    ]
```

### Libs:
Install the following libs using **pip install libname**:

- Python3.x
- cpf_generator
- geopy.geocoder

