#Hecho por Agustín Capogrossi
import numpy as np


def SOR (A, b, omega,err,mit):
	#Inicializamos las variables
	A = np.array(A)
	n = A.shape[0]
	x = np.zeros(n)
	x_n = np.zeros(n)
	k = 0
	#Primera condición de STOP, cuando las iteraciones superan el maximo de iteraciones
	while k<mit:
		for i in range (A.shape[0]):
			#Almacenamos los valores temporales en una variable
			s = 0
			for j in range (A.shape[1]):
				if j != i:
				#Aplicamos la formula de recursión
					s = s + A[i][j] * x[j]
			x_n[i] = (1 - omega) * x_n[i] + (omega/A[i][i])*(b[i] - s)
		#Segunda condición de STOP, cuando la norma infinito es menor que la tolerancia dada
		if np.linalg.norm(x_n - x, np.inf)<= err:
			print('La norma infinito de la diferencia es menor que la tolerancia dada')
			return x_n,k
		#Actualizamos los valores
		x = x_n
		x_n = np.zeros(n)
		k+=1
	return x,k

