def superpower(a,b):
	r=1
	for c in range (b):
		r=r*a
	return r
Base=int(input("Cual sera el valor de la base: "))
Potencia=int(input("Cual es el valor de la potencia: "))
print ("El resultado de %s elevado a la %s es:"%(Base,Potencia),superpower(Base,Potencia))
