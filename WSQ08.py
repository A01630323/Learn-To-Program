def Menu():
	print ("************************************")
	print ("*** CALCULADORA USANDO FUNCIONES ***")
	print ("************************************")
#
def Suma(N1,N2):
    Suma = N1 + N2
    return Suma
#
def Resta(N1,N2):
	Resta = N1 - N2
	return Resta
#
def Multiplicacion(N1,N2):
	Multiplicacion = N1 * N2
	return Multiplicacion
#
def Divicion(N1,N2):
	Divicion = int(N1 / N2)
	return Divicion
#
def Modulo(N1,N2):
	Modulo = N1 % N2
	return Modulo
#
def Resultados(RSuma,RResta,RMultiplicacion,RDivicion,RModulo):
	print ("El resultado de la SUMA es: ",RSuma)
	print ("El resultado de la RESTA es: ",RResta)
	print ("El resultado de la MULTIPLICACION es: ",RMultiplicacion)
	print ("El resultado de la DIVICION es: ",RDivicion)
	print ("El resultado del MODULO es: ",RModulo)
#
def Salir():
        print ("********************")
        print ("GRACIAS, hasta luego")
        print ("********************")
#
Menu()
Numero1=int(input("Dame el primer numero: "))
Numero2=int(input("Dame el segundo numero: "))
Resultado1=Suma(Numero1,Numero2)
Resultado2=Resta(Numero1,Numero2)
Resultado3=Multiplicacion(Numero1,Numero2)
Resultado4=Divicion(Numero1,Numero2)
Resultado5=Modulo(Numero1,Numero2)
Resultados(Resultado1,Resultado2,Resultado3,Resultado4,Resultado5)
Salir()
input ()