
import numpy as np
import matplotlib.pyplot as plt

from llenarClase import *
from Orden import *
from datosGrafica import *

lista= llenarClase()
data= datosGrafica(lista)
tipos=data[0]
carnes= data[1]
ingredientes=data[2]

total_carnes= sum(carnes)

labels = "Asada","Adobada","Cabeza","Lengua","Suadero","Veggie","Tripa"
fracs = [carnes[0]/total_carnes,carnes[1]/total_carnes,carnes[2]/total_carnes,carnes[3]/total_carnes,
         carnes[4]/total_carnes,carnes[5]/total_carnes,carnes[6]/total_carnes]

N = 5
cantidad = (1000-ingredientes[0],1000-ingredientes[1],1000-ingredientes[2],1000-ingredientes[3],1000-ingredientes[4])
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

rows = ["Tacos", "Quesadilla", "Mulita", "Tostada", "Vampiro", "Orden"]
columns = ["Asada", "Adobada", "Cabeza", "Lengua", "Suadero", "Veggie", "Tripa"]

data_list = np.random.randint(0,1, size=(len(rows), len(columns)))

fig1, axs =plt.subplots(2,1)
axs[0].axis('tight')
axs[0].axis('off')
the_table = axs[0].table(cellText=data_list,
          rowLabels=rows,
          colLabels=columns, loc="upper center")
axs[0].set_title("Tipos y Carnes")
axs[1].set_title("Ingredientes disponibles")
axs[1].set_xticklabels([" ","Cebolla","Salsa","Cilantro","Aguacate","Frijoles"])
axs[1].bar(ind, cantidad, width)

fig2= plt.figure()
ax = fig2.add_subplot(111)
ax.set_title("Porcentaje de carnes consumidas")
ax=plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)

axs[0].set_axis_off
axs[1].set_axis_off

fig1.show()
fig2.show()

input()
