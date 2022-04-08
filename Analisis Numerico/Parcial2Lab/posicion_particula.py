#Hecho por Agustín Capogrossi
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.interpolate

#Definimos la tabla
x = [0.0, 0.22, 0.85, 1.0, 1.5, 1.6, 1.99]
y = [0.0,0.1,-0.15,-0.03,0.75,-0.3,0.01]
#Definimos n como el tamaño de x
n = len(x)

def posicion_particula(x,y):
	S = 0.0
	h = 0.0
	posicion = [0.0]
	#Agregamos los valores medios de los elementos consecutivos de x
	for i in range(n-1):
		a = x[i]
		b = x[i+1]
		h = (b-a)/2
		S = S + h*(y[i]+y[i+1])
		posicion.append(S) 
	print("La posición de la partícula en cada intervalo figura en la lista: ", posicion)
	#Graficamos la posicion de la partícula
	plt.plot(x,posicion, label='posicion')
	plt.legend()
	plt.show()
	return S
