import json
from Orden import *
import datetime as d

def obtenerOrdenes():
    listaOrdenes=[]
    with open("orden.json", 'r') as f:
        while True:
            line = f.readline()
            if line != "":
                data= json.loads(line)
            else:
                break
            for i in data:
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
                answer={}
                answer["Start Time"] = str(d.datetime.now())
                oc= OrdenCompleta(datetime,request,ordenes,answer)
            listaOrdenes.append(oc)
    return listaOrdenes

