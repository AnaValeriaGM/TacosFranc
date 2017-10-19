from llenarClases import *
from tomarOrden import *
from graficasProyecto import *
import sys

def main():
    mensaje= comenzar();

    listaOrdenes = llenarClases()

    graficas= graficasProyecto(listaOrdenes)
            
if __name__ == "__main__":
    main()
    sys.exit()
