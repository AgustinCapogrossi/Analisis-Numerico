#Hecho por Agustín Capogrossi
#         tiempo  planchas precio
#mesas      2       1       500

#sillas     1       2       300

#total      40      50

# x: unidad de mesa
# y: unidad de silla


# Objetivo: f = x*500+y*300

#restricciones:
# 2*x + 1*y <= 40
# 1*x + 2*y <= 50
# x,y> = 0

# y <= 40 - 2*x
# y <= (50-x)/2

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,20,0.1)
#Establecemos las funciones lineales que determinan la region factible
y1 = (40-2*x)
y2 = (50-x)/2
#Queremos la zona debajo de la interseccion asi que creamos una variable que guarde este valor
y3 = np.minimum(y1,y2)

#Graficamos las funciones y la region 
plt.ylim(0,10)
plt.plot(x,y1, label='y1 = (40-2*x)')
plt.plot(x,y2, label='y2 = (50-x)/2')
plt.plot(x,y3,label='Region factible')
plt.fill_between(x,0,y3,2.5,alpha=0.5,color='green', hatch = '/')
plt.legend()
plt.show()

#Resolvemos el ejercicio
#Como linprog sirve para el minimo, calculamos el minimo de los opuestos asi obtenemos el valor opuesto del máximo

c = np.array([-500,-300])
A = np.array([[2,1],[1,2]])
b = np.array([40,50])
x0_bounds = (0, None)
x1_bounds = (0, None)

from scipy.optimize import linprog

res = linprog(c, A_ub = A, b_ub = b, bounds = [x0_bounds,x1_bounds])
print(res)

