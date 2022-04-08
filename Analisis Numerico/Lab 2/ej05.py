import math

def ripf(fun,x0,err,mit):
	k = 1
	hx = [x0]
	fun(x0) = f
	while k<mit:
		xn = f
		
		if abs(xn-x0)<err
			print("El paso es pequeño")
			return hx
		x0 = xn
		f = fun(x0)
		hx.append(x0)
		k = k+1
	return hx
		 
