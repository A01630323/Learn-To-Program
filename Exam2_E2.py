def triangulo(size):
	for a in range (1,size+1,1):
		for b in range (1,a+1):
			print ("T",end='')
		print ()
	for a in range (size,0,-1):
		for b in range (1,a+1):
			print ("T",end='')
		print ()
Numero=int(input("Cantidad de triangulos a mostrar: "))
triangulo(Numero)
