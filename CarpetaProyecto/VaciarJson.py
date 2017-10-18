import json

def vaciarJson(archivo):
    with open(archivo, 'r') as data_file:
        data = json.load(data_file)

    for elemento in data:
        elemento.pop("", None) #Aqui irian los distintos elementos del diccionario

    with open(archivo, 'w') as data_file:
        data = json.dump(data, data_file)

def vaciado():
    vaciarJson(ordenesJSON.json)
