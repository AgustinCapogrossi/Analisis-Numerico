#Hecho por Agustín Capogrossi
import numpy as np

def soltrinf(A, b):
    n = A.shape[0]
    x = b
    
    for idx in range(n):
        for jdx in range(idx):
           x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x
def gseidel(A, b, err, mit): 
	A = np.array(A)
	n = A.shape[0]
	x = np.zeros(n)
	x_n = np.zeros(n)
	k = 0
	#Condicion de STOP, cuando se superen las iteraciones dadas
	while k < mit:
		#Recorremos el array
		for i in range(n):
			#Guardamos en s y en t los valores temporales
			s = 0
			t = 0
			for j in range(n):
				if j<i:
					s = s + A[i,j] * x_n[j]
				if j>i:
					t = t + A[i,j] * x[j]
			#Aplicamos la formula de recursión
			x_n[i] = (b[i]-(s+t))/A[i,i]
		#Segunda condición de STOP, cuando la norma infinito es menor que la tolerancia dada
		if np.linalg.norm(x_n - x, np.inf) <= err:
			print('La norma infinito de la diferencia es menor que la tolerancia dada')
			return x_n,k
        #Actualizamos los valores
		x = x_n
		x_n = np.zeros(n)
		k+=1
        
	return x, k
