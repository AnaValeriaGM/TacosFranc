from llenarClases import *
from tomarOrden import *
from graficasProyecto import *

def main():
    mensaje= tomarOrden();

    listaOrdenes = llenarClases()

    graficas= graficasProyecto(listaOrdenes)
            
if __name__ == "__main__":
    main()
    sys.exit()
