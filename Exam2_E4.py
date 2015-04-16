def fibonacci(n):
	if (n==0):
		return 0
	elif (n==1):
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
Numero=int(input("De que numero deceas calcular la sucesion de fibonacci (numero positivo): "))
if (Numero<0):
	print ("No se calculara la sucesion de fibonacci de un numero negativo")
else:
	print ("El resultado es: ",fibonacci(Numero))
