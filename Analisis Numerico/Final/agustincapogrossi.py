#
#Recurso							Resistencia Normal		Resistencia Alta	Disponibilidad		

# Materia prima utilizada				7m^3/ton				11m^3/ton			77m^3/ton

# Tiempo requerido de producción		10hs/ton				8hs/ton				80hs/ton	

# Almacenamiento						9ton					6ton

# Utilidad/beneficio por tonelada		150COP/ton				175COP/ton

#x: una tonelada de concreto con resistencia normal
#y: una tonelada de concreto con resistencia alta

#	B(x,y) = x*150 + y*170
#	7x+11y <= 77
#	10x+8y <= 80
#	0<x<9
#	0<y<6


# Resolviendo

#	y = (77-7x)/11
#	y = (80-10x)/8
#	funcion objetivo f = x*150+y*170

#

import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,20,0.1)

y1 = (77-7*x)/4
y2 = (80-10*x)/8
y3 = np.minimum(y1,y2)
y4 = 0.0000001*x+6	#Una aproximación a y=6
y5 = -1000/30*x+300	#Una aproximación a x=9
y6 = np.minimum(y4,y5)
y7 = np.minimum(y3,y6) #Calcular el area que todas estas funciones tienen en comun

#Gráfica del ejercicio
plt.ylim(0,20)
plt.plot(x,y1,label= "f(x)=(77-7/x)/4")
plt.plot(x,y2,label= "f(x)=(80-10*x)/8")
plt.plot(x,y4, label= "y<6")
plt.plot(x,y5, label= "x<9")
plt.legend()
plt.xlabel("Resistencia Normal")
plt.ylabel("Resistencia Alta")
plt.fill_between(x,0,y7)
plt.show()

#Resolución del ejercicio
c = np.array([-150, -170])
A = np.array([ [7,10], [11,8] ])
b = np.array([77,80])
x0_bounds = (0, None)
x1_bounds = (0, None)

from scipy.optimize import linprog

res = linprog(c, A_ub = A, b_ub = b, bounds=[x0_bounds, x1_bounds])
#El resultado impreso para la máxima ganancia que puede obtener la empresa está en negativo, pero su valor absoluto es el valor correcto.
print(res)



