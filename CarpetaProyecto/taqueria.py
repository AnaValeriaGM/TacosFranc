
import time as t
import datetime as d
import queue as q
from threading import Thread
from obtenerOrdenes import *

ingredientes = {"guacamole": 500,
                "cebolla": 500,
                "cilantro": 500,
                "frijoles": 500,
                "salsa": 500,
                "tortillas" : 500}
estadisticasTipo= {"taco" : 0,
               "mulita" : 0,
               "quesadilla" : 0,
               "tostada" : 0,
               "vampiro": 0}
estadisticasCarne={"asada":0,
                   "adobada":0,
                   "cabeza":0,
                   "lengua":0,
                   "suadero":0,
                   "veggie":0,
                   "tripa":0}
estadisticasIngredientes={"guacamole": 0,
                "cebolla": 0,
                "cilantro": 0,
                "frijoles": 0,
                "salsa": 0}
taqueroAsada = q.Queue()
taqueroAdobada= q.Queue()
taqueroOtros = q.Queue()
global respuesta
respuesta = []

def reFill(ingrediente):
    t.sleep(2)
    ingredientes[ingrediente]+=50

def mandarTaquero(listaOrdenes):
    global respuesta
    while len(listaOrdenes) > 0:
        orden = listaOrdenes.pop(0)
        for suborden in orden.orden:
            carne = suborden.carne
            if carne == "asada":
                taqueroAsada.put(suborden)
            elif carne == "adobada":
                taqueroAdobada.put(suborden)
            else:
                taqueroOtros.put(suborden)
        orden.answer["End Time"] = str(d.datetime.now())
        orden.answer["Terminado"] = "Yes"
        respuesta.append(orden)
                
def hacerOrden(orden):
    if orden != None:
        if ingredientes["guacamole"] <= 0:
            reFill("guacamole")
        if ingredientes["cebolla"] <=0:
            reFill("cebolla")
        if ingredientes["cilantro"] <= 0:
            reFill("cilantro")
        if ingredientes["frijoles"] <= 0:
            reFill("frijoles")
        if ingredientes["salsa"] <= 0:
            reFill("salsa")
        if ingredientes["tortillas"] <= 0:
            reFill("tortillas")
        if "guacamole" in orden.ingredientes:
            if ingredientes["guacamole"] < orden.cantidad:
                reFill("guacamole")
            ingredientes["guacamole"] -= orden.cantidad
        if "cebolla" in orden.ingredientes:
            if ingredientes["cebolla"] < orden.cantidad:
                reFill("cebolla")
            ingredientes["cebolla"] -= orden.cantidad
        if "cilantro" in orden.ingredientes:
            if ingredientes["cilantro"] < orden.cantidad:
                reFill("cilantro")
            ingredientes["cilantro"] -= orden.cantidad
        if "frijoles" in orden.ingredientes:
            if ingredientes["frijoles"] < orden.cantidad:
                reFill("frijoles")
            ingredientes["frijoles"] -= orden.cantidad
        if "salsa" in orden.ingredientes:
            if ingredientes["salsa"] < orden.cantidad:
                reFill("salsa")
            ingredientes["salsa"] -= orden.cantidad
        if ingredientes["tortillas"] < orden.cantidad:
                reFill("tortillas")
        ingredientes["tortillas"] -= orden.cantidad
        t.sleep(1*orden.cantidad)
        print("Listo")
        print(ingredientes)
    else:
        return

def taquero(queue,nombre):
    respuesta=[]
    while queue.qsize() > 0:
        orden = hacerOrden(queue.get())
        t.sleep(3)
    print("Termino: ",nombre)

def start():
    ordenes= obtenerOrdenes()
    mandarTaquero(ordenes)
    threadTaquero1 = Thread(target=taquero, args=(taqueroAsada,"El Pariente (Asada)",))
    threadTaquero1.start()
    threadTaquero2 = Thread(target=taquero, args=(taqueroAdobada,"El Flaco(Adobada)",))
    threadTaquero2.start()
    threadTaquero3 = Thread(target=taquero, args=(taqueroOtros,"El Wero (Otros)",))
    threadTaquero3.start()
    threadTaquero1.join()
    threadTaquero2.join()
    threadTaquero3.join()
##    while True:
##        ordenes.extend(obtenerOrdenes)
start= start()
from data import *
