def Titulo():
	print ("*************************")
	print ("*** ARCHIVOS DE TEXTO ***")
	print ("*************************")
def Carros():
	Archivo=open("93Cars.txt","r")
	GasCiudad=0
	GasCarretera=0
	Precio=0
	Contador=1
	for Linea in Archivo:
		if (Contador%2==1):
			Precio=Precio+float(Linea[42:46])
			GasCiudad=GasCiudad+float(Linea[52:54])
			GasCarretera=GasCarretera+float(Linea[55:57])
		Contador=Contador+1
	print("El promedio de gas usado en la ciudad es " ,GasCiudad/(len(Linea)/2))
	print("El promedio de gas usado en la carretera es: " ,GasCarretera/(len(Linea)/2))
	print("El precio promedio de un auto de gama media es: " ,Precio/(len(Linea)/2))
#
Titulo()
Carros()
input()
