import math
def rbisec(fun,I,err,mit):
	a = I[0]
	b = I[1]
	
	k = 0.0
	
	hx = []
	hf = []
	
	if fun(a)*fun(b) < 0.0:
		c = (b-a)/2.0
		hx.append(c)
		hf.append(fun(c))
		while k<mit and abs(fun(c))<err:
			k = k+1
			if (fun(c)*fun(a)<0.0):
				b = c
			else:
				a = c
			c = (a+b)/2.0
			hx.append(c)
			hf.append(fun(c))
	else:
		print("Intervalo invalido")
	return hx,hf
		
