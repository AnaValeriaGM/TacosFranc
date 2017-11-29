
from estadisticas import *
from graficas import *
from obtenerOrdenes import *
import sys

listaOrdenes= obtenerOrdenes()
data= datosGrafica(listaOrdenes)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.tipos= data[0]
ui.carnes= data[1]
ui.ingredientes= data[2]
ui.agregarGraficas()
MainWindow.show()

