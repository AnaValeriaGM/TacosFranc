
from Orden import *

def datosGrafica(listaOrden):
    l= listaOrden
    datos=[[],[],[]]
    tipo=porTipo(l)
    carne=porCarne(l)
    ingredientes=porIngredientes(l)
    datos[0]=tipo
    datos[1]=carne
    datos[2]=ingredientes
    return datos

def porTipo(listaOrden):
    contadores= []
    contadorTaco=0
    contadorQuesadilla=0
    contadorTostada=0
    contadorMulitas=0
    contadorVampiro=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].tipo == "taco":
                contadorTaco+=i.orden[j].cantidad
            if i.orden[j].tipo == "quesadilla":
                contadorQuesadilla+=i.orden[j].cantidad
            if i.orden[j].tipo== "tostada":
                contadorTostada+=i.orden[j].cantidad
            if i.orden[j].tipo== "mulita":
                contadorMulitas+=i.orden[j].cantidad
            if i.orden[j].tipo== "vampiro":
                contadorVampiro+=i.orden[j].cantidad
    contadores.append(contadorTaco)   
    contadores.append(contadorQuesadilla)        
    contadores.append(contadorTostada)       
    contadores.append(contadorMulitas)      
    contadores.append(contadorVampiro)
    return contadores

def porCarne(listaOrden):
    contadores= []
    contadorAsada=0
    contadorAdobada=0
    contadorCabeza=0
    contadorLengua=0
    contadorSuadero=0
    contadorVeggie=0
    contadorTripa=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if i.orden[j].carne == "asada":
                contadorAsada+=i.orden[j].cantidad
            if i.orden[j].carne == "adobada":
                contadorAdobada+=i.orden[j].cantidad
            if i.orden[j].carne == "cabeza":
                contadorCabeza+=i.orden[j].cantidad
            if i.orden[j].carne == "lengua":
                contadorLengua+=i.orden[j].cantidad
            if i.orden[j].carne == "suadero":
                contadorSuadero+=i.orden[j].cantidad
            if i.orden[j].carne == "veggie":
                contadorVeggie+=i.orden[j].cantidad
            if i.orden[j].carne== "tripa":
                contadorTripa+=i.orden[j].cantidad
    contadores.append(contadorAsada)   
    contadores.append(contadorAdobada)   
    contadores.append(contadorCabeza)
    contadores.append(contadorLengua)    
    contadores.append(contadorSuadero)
    contadores.append(contadorVeggie)        
    contadores.append(contadorTripa)
    return contadores

def porIngredientes(listaOrden):
    contadores= []
    contadorCebolla=0
    contadorSalsa=0
    contadorCilantro=0
    contadorAguacate=0
    contadorFrijol=0
    for i in listaOrden:
        largo= len(i.orden)
        for j in range(largo):
            if "cebolla" in i.orden[j].ingredientes:
                contadorCebolla+=i.orden[j].cantidad
            if "salsa" in i.orden[j].ingredientes:
                contadorSalsa+=i.orden[j].cantidad
            if "cilantro" in i.orden[j].ingredientes:
                contadorCilantro+=i.orden[j].cantidad
            if "aguacate" in i.orden[j].ingredientes:
                contadorAguacate+=i.orden[j].cantidad
            if "frijol" in i.orden[j].ingredientes:
                contadorFrijol+=i.orden[j].cantidad
    contadores.append(contadorCebolla)     
    contadores.append(contadorSalsa)
    contadores.append(contadorCilantro)     
    contadores.append(contadorAguacate)      
    contadores.append(contadorFrijol)
    return contadores
