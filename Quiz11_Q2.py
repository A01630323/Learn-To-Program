def checkbanana(Datos):
	Archivo=open(Datos,"r")													#Lee el archivo en modo lectura
	ContadorBananas=0
	Banana="banana"															#La palabra a buscar en el archivo de texto sera "banana"
	Medida=len(Banana)
	for Linea in Archivo:													#Analizar cada linea del archivo de texto
		Linea=Linea.lower()													#Convertir toda la linea en letras minusculas
		Posicion=Linea.find(Banana)											#Buscar la palabra "banana" dentro de la linea
		while (Posicion!=-1):												#Mientras "banana" sea encontrada en el documento
			ContadorBananas=ContadorBananas+1								#Indicarlo
			Posicion=Linea.find(Banana,Posicion+Medida)						#Continuar buscando a partir de la ultima banana encontrada
	print ("En el documento se encontraron %s bananas"%(ContadorBananas))
#
checkbanana("Banana.txt")
