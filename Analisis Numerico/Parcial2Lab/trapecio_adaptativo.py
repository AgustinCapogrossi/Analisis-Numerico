#Hecho por Agustín Capogrossi
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.interpolate

#Definimos la lista
x = [0.0, 0.22, 0.85, 1.0, 1.5, 1.6, 1.99]
y = [0.0,0.1,-0.15,-0.03,0.75,-0.3,0.01]
#Definimos n como el tamaño de x
n = len(x)
def trapecio_adaptativo(x,y):
	S = 0.0
	h = 0.0
	#Adaptamos la formula del trapecio
	for i in range(n-1):
		a = x[i]
		b = x[i+1]
		h = (b-a)/2
		S = S + h*(y[i]+y[i+1]) 
	print("Aproximación de la integral: ",S)
	
