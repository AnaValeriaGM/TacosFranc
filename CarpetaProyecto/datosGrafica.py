
from llenarClases import*
from Orden import *

def datosGrafica(listaOrden):
    l= listaOrden
    datos=[]
    tipo=porTipo(l)
    carne=porCarne(l)
    ingredientes=porIngredientes(l)

    datos.append(tipo)
    datos.append(carne)
    datos.append(ingredientes)

    return datos

def porTipo(listaOrden):
    contadores= []
    contadorTaco=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].tipo == "taco":
                contadorTaco+=i.orden[j].cantidad
    contadores.append(contadorTaco)   
    contadorQuesadilla=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].tipo == "quesadilla":
                contadorQuesadilla+=i.orden[j].cantidad
    contadores.append(contadorQuesadilla)        
    contadorTostada=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].tipo== "tostada":
                contadorTostada+=i.orden[j].cantidad
    contadores.append(contadorTostada)       
    contadorMulitas=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].tipo== "mulita":
                contadorMulitas+=i.orden[j].cantidad
    contadores.append(contadorMulitas)      
    contadorVampiro=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].tipo== "vampiro":
                contadorVampiro+=i.orden[j].cantidad
    contadores.append(contadorVampiro)
    return contadores

def porCarne(listaOrden):
    contadores= []
    contadorAsada=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].carne == "asada":
                contadorAsada+=i.orden[j].cantidad
    contadores.append(contadorAsada)   
    contadorAdobada=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].carne == "adobada":
                contadorAdobada+=i.orden[j].cantidad
    contadores.append(contadorAdobada)   
    contadorCabeza=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].carne == "cabeza":
                contadorCabeza+=i.orden[j].cantidad
    contadores.append(contadorCabeza)
    contadorLengua=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].carne == "lengua":
                contadorLengua+=i.orden[j].cantidad
    contadores.append(contadorLengua)    
    contadorSuadero=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].carne == "suadero":
                contadorSuadero+=i.orden[j].cantidad
    contadores.append(contadorSuadero)
    contadorVeggie=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].carne == "veggie":
                contadorVeggie+=i.orden[j].cantidad
    contadores.append(contadorVeggie)        
    contadorTripa=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].carne== "tripa":
                contadorTripa+=i.orden[j].cantidad
    contadores.append(contadorTripa)
    return contadores

def porIngredientes(listaOrden):
    contadores= []
    contadorCebolla=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if "cebolla" in i.orden[j].ingredientes:
                contadorCebolla+=i.orden[j].cantidad
    contadores.append(contadorCebolla)     
    contadorSalsa=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if "salsa" in i.orden[j].ingredientes:
                contadorSalsa+=i.orden[j].cantidad
    contadores.append(contadorSalsa)
    contadorCilantro=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if "cilantro" in i.orden[j].ingredientes:
                contadorCilantro+=i.orden[j].cantidad
    contadores.append(contadorCilantro)     
    contadorAguacate=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if "aguacate" in i.orden[j].ingredientes:
                contadorAguacate+=i.orden[j].cantidad
    contadores.append(contadorAguacate)      
    contadorFrijol=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if "frijol" in i.orden[j].ingredientes:
                contadorFrijol+=i.orden[j].cantidad
    contadores.append(contadorFrijol)
    return contadores
