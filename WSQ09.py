print ("*****************")
print ("*** FACTORIAL ***")
print ("*****************")
Salir="n"
Resultado=1
Contador=1
while(Salir!="s" and Salir!="S"):
	Factorial=int(input("DE QUE NUMERO DECEAS EL FACTORIAL: "))
	if (Factorial>=0):
		if (Factorial==0):
			Resultado=1
		else:
			while (Contador<=Factorial):
				Resultado=Resultado*Contador
				Contador=Contador+1
		print ("El resultado del factorial es: ",Resultado)
	else:
		print ("Lo siento, en este programa no calcularemos factoriales <0")
	Salir=input("\n\t¿Deceas salir del programa?. Pulsa \"s\" o \"S\ ")