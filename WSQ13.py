def Titulo():
	print ("*************************")
	print ("*** METODO BABILONICO ***")
	print ("*************************")
#
def Raiz(X):
	R=X
	T=0
	while (T!=R):
		T=R
		R=(X/R+R)/2
	return R
#
Titulo()
Radicando=int(input("Coloca el valor del radicando: "))
Resultado=Raiz(Radicando)
print ("El resultado de la raiz cuadrada por el metodo babilonico es: ",Resultado)
input ()
