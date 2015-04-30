def Titulo():
	print ("***********************")
	print ("*** VALIDAR ENTRADA ***")
	print ("***********************")
#
def Area(Lado):
	print ("El area del cuadrado es: ",Lado**2)
#
def Entrada():
	while (True):
		try:
			Entrada=int(input("Dame el valor de un lado del cuadrado (solo numeros enteros): "))
			break
		except ValueError:
			print("El dato colocado NO ES UN NUMERO ENTERO.")
	Area(Entrada)
#
Titulo()
Entrada()
input ()
