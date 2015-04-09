def Titulo():
	print ("*******************************")
	print ("*** FIBONACCI POR RECURSION ***")
	print ("*******************************")
#
def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
#
Titulo()
Numero=int(input("Numero que deceas calcular la sucesión de fibonacci: "))
print ("El resultado es: ",fib(Numero))
input ()
