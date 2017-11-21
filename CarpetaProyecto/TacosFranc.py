from llenarClases import *
from tomarOrden import *
from graficasProyecto import *
import sys

def main():
    mensajes= comenzar();

    listaOrdenes = llenarClases()

    graficas= graficasProyecto(listaOrdenes)
            
if __name__ == "__main__":
    main()
    sys.exit()
