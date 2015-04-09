def Titulo ():
	print ("*********************************")
	print ("*** FACTORIAL POR INTERACCION ***")
	print ("*********************************")
#
def factorial(n):
	Resultado=1
	while (n>=1):
		Resultado=Resultado*n
		n=n-1
	return Resultado
#
Titulo ()
Numero=int(input("De que numero deceas el factorial: "))
print ("El resultado del factorial es: ",factorial(Numero))
input()
