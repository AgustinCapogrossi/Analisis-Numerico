import random

def vander(n,m):
	for i in range (1,n+1):
		for j in range (1,m+1):
			print("A({},{}) = {}".format(i,j,1/(i+j)))
			
def suma_aleatorio(Tol):
	s = 0
	contador = 0
	
	while s <= Tol:
		s = s+random.random()
		contador = contador+1
	
	return s,contador
	
