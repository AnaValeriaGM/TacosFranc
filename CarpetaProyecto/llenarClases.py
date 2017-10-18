
import json
from Orden import *

def llenarClases():
    listaOrdenes=[]
    with open("ordenesJSON.json") as json_file:
        data_json = json.load(json_file)

        for data in data_json:
            ordenes=[]

            datetime=data["datetime"]
            request=data["request_id"]
            for i in range(len(data["orden"])):
                o= Orden(data["orden"][i]["part_id"],
                         data["orden"][i]["type"],
                         data["orden"][i]["meat"],
                         data["orden"][i]["quantity"],
                         data["orden"][i]["ingredients"])
                ordenes.append(o)    
            answer=data["answer"]

            oc= OrdenCompleta(datetime,request,ordenes,answer)
            listaOrdenes.append(oc)
    return listaOrdenes 

##ordenes= llenarClases()
##print(ordenes)
##for i in range(len(ordenes.orden)):
##    print(ordenes.orden[i])
