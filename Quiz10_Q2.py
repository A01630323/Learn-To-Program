def dotProduct(Lista1,Lista2):
	if (len(Lista1)==len(Lista2)):
		Suma=0
		for a in range (len(Lista1)):
			Suma=Suma+(Lista1[a]*Lista2[a])
		return Suma
	else:
		print ("Not same size vectors")
		return -1
#
def Llenar():
	Elemento=int(input("Numero de elementos: "))
	Lista=[0]*Elemento
	n=0
	while(n<Elemento):
		Lista[n]=int(input("Numero a almacenar en la lista: "))
		n=n+1
	return Lista
#
print ("**********")
print ("LISTA 1")
Dato1=Llenar()
print ("**********")
print ("LISTA 2")
Dato2=Llenar()
print ("**********")
print (dotProduct(Dato1,Dato2))
