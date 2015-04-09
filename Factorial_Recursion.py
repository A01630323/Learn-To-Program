def Titulo ():
	print ("*******************************")
	print ("*** FACTORIAL POR RECURSION ***")
	print ("*******************************")
#
def factorial(n):
	if (n==0):
		return 1
	else:
		return n*factorial(n-1)
#
Titulo ()
Numero=int(input("De que numero deceas el factorial: "))
print ("El resultado del factorial es: ",factorial(Numero))
input()
