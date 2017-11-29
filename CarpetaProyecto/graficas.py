import random as r
import math
import numpy as np
from PyQt5 import QtGui,QtWidgets

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class Graficas(FigureCanvas):
    
    def __init__ (self, tipos,carnes,ingredientes,parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)

        self.tipos= tipos
        self.carnes= carnes
        self.ingredientes= ingredientes

        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()

    def compute_initial_figure(self):
        self.Grafica1 = [["Taco","Quesadilla","Tostada","Mulita","Vampiro"],
                         [self.tipos[0],self.tipos[1],self.tipos[2],self.tipos[3],self.tipos[4]],
                         [0,0,0,0,0],
                         [0,0,0,0,0],
                         [0,0,0,0,0],
                         [0,0,0,0,0]]
        self.Grafica2 = [['Asada', 'Adobada', 'Cabeza','Lengua','Suadero','Veggie', 'Tripa'], self.carnes]
        self.Grafica3 = [["K","L","M","N","O"],
                         [r.randint(0,100),r.randint(0,100),r.randint(0,100),r.randint(0,100),r.randint(0,100)],
                         [r.randint(0,100),r.randint(0,100),r.randint(0,100),r.randint(0,100),r.randint(0,100)]]
        self.Grafica4 = [["P","Q","S","T","U"], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.Grafica5 = [["V","W","X","Y","Z"], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.data = {"Grafica 1" : self.Grafica1,
                     "Grafica 2" :  self.Grafica2,
                     "Grafica 3" :  self.Grafica3,
                     "Grafica 4" :  self.Grafica4,
                     "Grafica 5" :  self.Grafica5}
        self.updatefig("Grafica 1")

    def updatefig(self, text):
        if self.data[text] == self.Grafica1:
            self.plot1(self.data[text])
        elif self.data[text] == self.Grafica2:
            self.plot2(self.data[text])
        elif self.data[text] == self.Grafica3:
            self.plot3(self.data[text])
        elif self.data[text] == self.Grafica4:
            self.plot4(self.data[text])
        elif self.data[text] == self.Grafica5:
            self.plot5(self.data[text])

    def plot1(self, X_Y):
        self.axes.clear()
        summedX_Y = []
        for i in range(len(X_Y[0])-1):
            summedX_Y.append(X_Y[1][i] + X_Y[2][i] + X_Y[3][i] + X_Y[4][i] + X_Y[5][i])

        def roundup(x):
            return int(math.ceil(x / 10.0)) * 10

        N = len(X_Y[0])
        ind = np.arange(N)
        width = 0.75
        colors = ['yellowgreen', 'paleturquoise', 'royalblue', 'lightsteelblue', 'firebrick']

        p1 = self.axes.bar(ind, X_Y[1], width, color = colors[0])
        p2 = self.axes.bar(ind, X_Y[2], width, bottom = X_Y[1], color = colors[1])
        p3 = self.axes.bar(ind, X_Y[3], width, bottom = [x + y for x, y in zip(X_Y[1], X_Y[2])], color = colors[2])
        p4 = self.axes.bar(ind, X_Y[4], width, bottom = [x + y + z for x, y, z in zip(X_Y[1], X_Y[2], X_Y[3])], color = colors[3])
        p5 = self.axes.bar(ind, X_Y[5], width, bottom = [x + y + z + i for x, y, z, i in zip(X_Y[1], X_Y[2], X_Y[3], X_Y[4])], color = colors[4])

        countrylabels=["Tacos","Quesadillas","Mulita","Tostada","Vampiro"]

        self.axes.set_ylabel('Cantidad')
        self.axes.set_title('Tipos de tacos')
        self.axes.set_xticks(ind)
        self.axes.set_xticklabels(countrylabels, fontsize = 8)
        self.axes.set_yticklabels(np.arange(0, 1000000, roundup(max(summedX_Y) / 10)))
        self.axes.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Cebolla', 'Salsa', 'Cilantro', 'Aguacate', 'Frijoles'))
        self.draw_idle()
    def plot2(self, X_Y):
        self.axes.clear()
        labels = ['Adobada', 'Asada', 'Cabeza','Lengua','Suadero','Veggie', 'Tripa']
        sizes = X_Y[1]
        explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1) 
        self.axes.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        self.draw_idle()
    def plot3(self,X_Y):
        self.axes.clear()
        x= X_Y[1]
        y= X_Y[2]
        self.axes.plot(x,y)
        self.draw_idle()
    def plot4(self,X_Y):
        self.axes.clear()
        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)
        self.axes.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
        self.axes.set_xlabel('Smarts')
        self.axes.set_ylabel('Probability')
        self.axes.set_title('Histogram of IQ')
        self.draw_idle()
    def plot5(self,X_Y):
        self.axes.clear()
        data = [[ 66386, 174296,  75131, 577908,  32015],
        [ 58230, 381139,  78045,  99308, 160454],
        [ 89135,  80552, 152558, 497981, 603535],
        [ 78415,  81858, 150656, 193263,  69638],
        [139361, 331509, 343164, 781380,  52269]]

        columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
        rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
        self.axes.table(cellText=data,
                      rowLabels=rows,
                      colLabels=columns,
                      loc='center')
        self.draw_idle()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.l = QtWidgets.QVBoxLayout(self.main_widget)

        self.main_widget.setFocus()
        MainWindow.setCentralWidget(self.main_widget)
        MainWindow.setWindowTitle("Proyecto Final")

        self.tipos=[1,1,1,1,1]
        self.carnes=[1,1,1,1,1,1,1]
        self.ingredientes=[1,1,1,1,1]

        self.graficas = Graficas(self.tipos,self.carnes,self.ingredientes,
                                 self.main_widget, width = 10, height = 5, dpi = 100)
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.addItem('Grafica 1')
        self.comboBox.addItem('Grafica 2')
        self.comboBox.addItem('Grafica 3')
        self.comboBox.addItem('Grafica 4')
        self.comboBox.addItem('Grafica 5')


    def agregarGraficas(self):
        self.graficas = Graficas(self.tipos,self.carnes,self.ingredientes,
                                 self.main_widget, width = 10, height = 5, dpi = 100)
        self.comboBox.activated[str].connect(self.graficas.updatefig)
        self.l.addWidget(self.comboBox)
        self.l.addWidget(self.graficas)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
