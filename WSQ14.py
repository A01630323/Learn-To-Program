def Titulo():
	print ("*************************")
	print ("*** CALCULAR NUMERO e ***")
	print ("*************************")
#
def calculate_e(presicion):
	Result=1
	for Counter in range (1,500):
		Result=Result+(1/Factorial(Counter))
#Calcular el numero e tratando de hacerlo lo más exacto posible.La maxima presicion son 50 digitos, con 500 veces de repetir la ecuacion de Euler bastará.
#Realmente son 15 digitos los exactos, pues la variable Result no alcanza a almacenar los mas pequeños digitos, lo que ocaciona una distorción en los demas. 
#Además, se redondea el último digito mostrado por la utilización de la instruccion format
	return format(Result,'.%sf'%(presicion))				#Regresar valor con una presicion a la marcada por la variable
#
def Factorial(Numero):
	if (Numero==0):
		return 1
	else:
		return Numero*Factorial(Numero-1)
#
Titulo()
Q=int(input("Presicion: "))
print (calculate_e(Q))
input ()
