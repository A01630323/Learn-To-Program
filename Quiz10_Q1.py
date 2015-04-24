def Llenar():
	Elementos=int(input("Numero de Elementos: "))
	Lista=[0]*Elementos
	n=0
	while(n<Elementos):
		Lista[n]=int(input("Numero a almacenar en la lista: "))
		n=n+1
	return Lista
#
def findThrees(a):
    Suma=0
    for x in a:
        if (x%3==0):
          Suma=Suma+x
    return Suma
#
Numero=Llenar()
print ("The result is: ",findThrees(Numero))
