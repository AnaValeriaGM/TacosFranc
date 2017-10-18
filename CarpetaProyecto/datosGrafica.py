
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
            
    contadorQuesadilla=0
    contadores.append(contadorQuesadilla)
    for i in listaOrden:
        if i.orden.tipo == "Quesadilla":
            contadorQuesadilla+=i.orden.cantidad
            
    contadorTostada=0
    contadores.append(contadorTostada)
    for i in listaOrden:
        if i.orden.tipo == "Tostada":
            contadorTostada+=i.orden.cantidad
            
    contadorMulitas=0
    contadores.append(contadorMulitas)
    for i in listaOrden:
        if i.orden.tipo == "Mulitas":
            contadorMulitas+=i.orden.cantidad
            
    contadorVampiro=0
    contadores.append(contadorVampiro)
    for i in listaOrden:
        if i.orden.tipo == "Vampiro":
            contadorVampiro+=i.orden.cantidad
    return contadores

def porCarne(listaOrden):
    contadores= []
    contadorAsada=0
    contadores.append(contadorTaco)
    for i in listaOrden:
        if i.orden.carne == "Asada":
            contadorAsada+=i.orden.cantidad
            
    contadorAdobada=0
    contadores.append(contadorAdobada)
    for i in listaOrden:
        if i.orden.carne == "Adobada":
            contadorAdobada+=i.orden.cantidad
            
    contadorCabeza=0
    contadores.append(contadorCabeza)
    for i in listaOrden:
        if i.orden.carne == "Cabeza":
            contadorCabeza+=i.orden.cantidad
            
    contadorLengua=0
    contadores.append(contadorLengua)
    for i in listaOrden:
        if i.orden.carne == "Lengua":
            contadorLengua+=i.orden.cantidad
            
    contadorSuadero=0
    contadores.append(contadorSuadero)
    for i in listaOrden:
        if i.orden.carne == "Suadero":
            contadorSuadero+=i.orden.cantidad
            
    contadorVeggie=0
    contadores.append(contadorVeggie)
    for i in listaOrden:
        if i.orden.carne == "Veggie":
            contadorVeggie+=i.orden.cantidad
            
    contadorTripa=0
    contadores.append(contadorTripa)
    for i in listaOrden:
        if i.orden.carne == "Tripa":
            contadorTripa+=i.orden.cantidad
    return contadores

def porIngrediente(listaOrden):
    contadores= []
    contadorCebolla=0
    contadores.append(contadorCebolla)
    for i in listaOrden:
        if "Cebolla" in i.orden.ingredientes:
            contadorCebolla+=i.orden.cantidad
            
    contadorSalsa=0
    contadores.append(contadorSalsa)
    for i in listaOrden:
        if "Salsa" in i.orden.ingredientes:
            contadorSalsa+=i.orden.cantidad
            
    contadorCilantro=0
    contadores.append(contadorCilantro)
    for i in listaOrden:
        if "Cilantro" in i.orden.ingredientes:
            contadorCilantro+=i.orden.cantidad
            
    contadorAguacate=0
    contadores.append(contadorAguacate)
    for i in listaOrden:
        if "Aguacate" in i.orden.ingredientes:
            contadorAguacate+=i.orden.cantidad
            
    contadorFrijol=0
    contadores.append(contadorFrijol)
    for i in listaOrden:
        if "Frijol" in i.orden.ingredientes:
            contadorFrijol+=i.orden.cantidad
    return contadores
