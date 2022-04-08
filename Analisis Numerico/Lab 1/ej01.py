def comparacion (x,y,z):
	a = x/y+z
	b = x/(y+z)
	c = x/y*z
	d = x/(y*z)
	print("Con x/y+z es igual a {}".format(a))
	print("Con x/(y+z) es igual a {}".format(b))
	if a>b:
		j = a-b
	else:
		j = b-a
	print("La diferencia entre x/y+z y x/(y+z) es {}".format(j))
	
	print("Con x/y*z es igual a {}".format(c))
	print("Con x/(y*z) es igual a {}".format(d))
	if c>d:
		i = c-d
	else:
		i = d-c
	print("La diferencia entre x/y*z y x/(y*z) es {}".format(i))
