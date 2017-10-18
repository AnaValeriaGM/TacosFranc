class Orden:
    def __init__(self,ine,tipo,carne,cantidad,ingredientes):
        self.ine=ine
        self.tipo=tipo
        self.carne=carne
        self.cantidad=cantidad
        self.ingredientes=ingredientes

    def __str__(self):
        return "\nID: {0}\nTipo: {1}\nCarne: {2}\nCantidad: {3}\nIngredientes: {4}\n".format(self.ine,self.tipo,self.carne,self.cantidad,self.ingredientes)

class OrdenCompleta:
    def __init__(self,datetime,request,orden,answer):
        self.datetime= datetime
        self.request= request
        self.orden= orden
        self.answer= answer

    def __str__(self):
        guiones= "--------------------------------------------------"
        return "Tiempo: {0}\nRequest ID: {1}\n{2}\nRespuesta: {3}\n{4}".format(self.datetime,self.request,self.orden,self.answer,guiones)

