#Hecho por Agustín Capogrossi
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.interpolate

x = [0.0, 0.22, 0.85, 1.0, 1.5, 1.6, 1.99]
y = [0.0,0.1,-0.15,-0.03,0.75,-0.3,0.01]
n = len(x)
#Utilizamos una lista temporal para almacenar todos los datos, a modo de no modificar la lista original
nx = []
#Agregamos los valores de x a nx
for j in range (n-1):
	nx.append(x[j])
#Calculamos los puntos medios entre ellos y los agregamos al final de la lista
for i in range(n-1):
	h = (x[i] + x[i+1])/2
	nx.append(h)

#Utilizamos scipy para evaluar con spline cubico
ny = sp.interpolate.interp1d(x, y, kind="cubic")(nx)

print("Todos los puntos de t en el intervalo [0,1.99] son y sus puntos medios son:",nx)
print("Los puntos de evaluación de un Spline cúbico de la función de velocidad en los puntos de la nueva partición son:",ny)
