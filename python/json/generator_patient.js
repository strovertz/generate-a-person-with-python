[
  '{{repeat(2, 2)}}',
  {
    // Template montado com funções JS fornecido por: https://json-generator.com/ 
    name: '{{firstName()}} {{surname()}}',
    username: '{{firstName()}}',
    email: '{{email()}}',
    gender: '{{gender()}}',
    person_id: "121",
    birthdate: "{{integer(2010, 2020)}}-{{integer(01, 12)}}-{{integer(01, 30)}}",
    documents: [
      {
        doctype: "CPF",
        rand_cpfnumber: "{{integer(11111111111, 99999999999)}}"
      }
    ],
    address: [
      {
        city: '{{street()}}',
        address_number: '{{integer(100, 999)}}',
        country_residence: '{{country()}}',
        province: '{{state()}}',        
        street: '{{city()}}',
        zip: '{{integer(100, 99999)}}'
      }
    ],        
    contacts: [
      {
        phones: [
          {
            phone_number: '{{integer(10, 99)}} {{integer(1, 9)}} {{integer(111111111, 999999999)}}', 
            type: "cellphone"     
          }
        ]
      }
    ] 
  } 
]
