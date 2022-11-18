import json
with open('myfile.json') as file:
    data = json.load(file)
    print(data[0]['gender'])
    with open('random_gender.txt') as infos:
        inf = infos.readlines()
        for int in range(1):
            data[int]['gender']
            print(data[int]['gender']) #teste 
            if data[int]['gender'] == "INSERT":
                data[int]['gender'] = inf[int]
out_file = open("new_data.json", "w")
json.dump(data, out_file, indent=6)