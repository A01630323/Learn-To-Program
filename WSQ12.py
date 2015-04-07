def Titulo():
	print ("***********************************")
	print ("*** ALGORITMO DE EUCLIDES (MCD) ***")
	print ("***********************************")
#
def MCD(A,B):
	while (B!=0):
		R=A%B
		A=B
		B=R
	return A
#
Titulo()
Numero1=float(input("Coloca el primer numero: "))
Numero2=float(input("Coloca el segundo numero: "))
Resultado=MCD(Numero1,Numero2)
print ("El MCD de los numeros %s y %s es:"%(Numero1,Numero2),Resultado)
input ()
