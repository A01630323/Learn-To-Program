import math																					#Importar modulos
#
def Titulo():																				#Funcion que escribe un titulo al programa
	print ("**************")
	print ("*** LISTAS ***")
	print ("**************")
#
def Llenar(Datos):																			#Funcion que llena elementos de la lista
	Contador=0
	Salir='S'
	while (Salir=="s" or Salir=="S"):
		if (Contador<=1):																		#La lista minimo tiene que tener dos valores. Asignarlos.
			Datos[Contador]=float(input("Dame el numero: "))
			Contador=Contador+1
		if (Contador>=2):																		#Si deceas añadir otros valores, simplemente pulsar "s" o "S"
			Salir=input("\n\t¿Deceas ingresar mas numeros?. Pulsa \"s\" o \"S\" : ")
			if (Salir=="s" or Salir=="S"):
				Datos.append(float(input("Dame el numero: ")))
	print ("La lista es: ",Datos)
	return Datos
#
def Suma(Datos):																			#Funcion que imprime la suma de la lista de numeros
	Suma=0
	Cantidad=len(Datos)																			#Conseguir la cantidad de elementos de la lista
	for Contador in range(0,Cantidad):
		Suma=Suma+Datos[Contador]
	print ("La suma de esos elementos es: ",Suma)
#
def Promedio(Datos):																		#Funcion que imprime el promedio de la lista de numeros
	Suma=0
	Cantidad=len(Datos)																			#Conseguir la cantidad de elementos de la lista
	for Contador in range(0,Cantidad):
		Suma=Suma+Datos[Contador]
	Promedio=Suma/Cantidad
	print ("El promedio de esos elementos es: ",Promedio)
#
def DesviacionEstandar(Datos):																#Funcion que imprime la desviacion estandar de los numeros
	Cantidad=len(Datos)																			#Conseguir la cantidad de elementos de la lista
	Sumatoria=0
	Cuadrados=1
	for Contador in range (0,Cantidad):															#Formula: stdev=sqrt((n^1)+(n+1^2)+(n+a^2))
		Cuadrados=Datos[Contador]**2																#Obtener el cuadrado del numero
		Sumatoria=Sumatoria+Cuadrados																#Sumar ese cuadrado
	Desviacion=math.sqrt (Sumatoria)
	print ("La desviacion estandar de esos elementos es: ",Desviacion)							#Sacar raiz cuandrada de la suma de cuadrados
#
Lista=[0]*2																					#Declarar una lista de 2 elementos para comenzar
Titulo()
Lista=Llenar(Lista)
Suma(Lista)
Promedio(Lista)
DesviacionEstandar(Lista)
input ()
