
from llenarClase import*
from Orden import *

def datosGrafica(listaOrden):
    l= listaOrden
    datos=[]
    tipo=porTipo(l)
    carne=porCarne(l)
    ingredientes=porIngredientes(l)

    datos.append(tipo)
    datos.appent(carne)
    datos.append(ingredientes)

    return datos

def porTipo(listaOrden):
    contadores= []
    contadorTaco=0
    contadores.append(contadorTaco)
    for i in listaOrden:
        if i.orden.tipo == "Taco":
            contadorTaco+=i.orden.cantidad
    return contadores

def porCarne(listaOrden):
    contadores= []
    contadorAsada=0
    contadores.append(contadorTaco)
    for i in listaOrden:
        if i.orden.carne == "Asada":
            contadorAsada+=i.orden.cantidad
    return contadores

def porIngrediente(listaOrden):
    contadores= []
    contadorCebolla=0
    contadores.append(contadorTaco)
    for i in listaOrden:
        if "Cebolla" in i.orden.ingredientes:
            contadorCebolla+=i.orden.cantidad
    return contadores
