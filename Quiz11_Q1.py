import random
import math
#
def readNumbersFromFile(Datos):
	Archivo=open(Datos,"r")											#Leer el archivo .txt
	Lineas=Archivo.readlines()										#Leer cada linea del archivo
	Suma=0
	SumaPotencias=1
	for a in Lineas:												#Analizar cada linea
		a=a.replace("\n","")										#Como al final del dato se colocó un salto de linea, debe suprimirse
		a=int(a)													#Ahora el dato debe convertirse en entero
		Suma=Suma+a													#Obtener la suma
		SumaPotencias=SumaPotencias+a**2							#Obtener la suma de cuadrados
	print ("El total es: ",Suma)
	print ("Las lineas del documento son: ",len(Lineas))
	print ("El promedio de los datos es: ",Suma/len(Lineas))
	print ("La desviacion estardar es: ",math.sqrt(SumaPotencias))
#
def CrearArchivo():
	Archivo=open("File.txt","w+")									#Crear un archivo .txt en modo sobreescritura
	a="\n"															#Salto de linea
	for b in range (random.randint(2,50)):							#Colocar entre 2 y 50 datos
		c=str(random.randint(-1000,1000))
		c=c+a														#El valor a escribir en la linea b debe ser de entre -1000 y 1000
		Archivo.writelines(c)										#Escribirlo en el documento
	Archivo.close													#Cerrar documento
	return Archivo.name												#Regresar el nombre del archivo
#
CrearArchivo()
Nombre=CrearArchivo()
readNumbersFromFile(Nombre)
