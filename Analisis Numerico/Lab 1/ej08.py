import math

def mala(a,b,c):

	x_1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
	
	x_1 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
	
def buena(a,b,c):
	if b >= 0:
        x_1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    
    else:
        x_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            
    x_2 = c / (a * x_1)
    
    return x_1, x_2    
