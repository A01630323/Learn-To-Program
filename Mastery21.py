def fib(n):																		#Calcular la sucesion de fibonacci por recursion
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
#
def Suma(n):																	#Calcular la suma de los primeros n numeros por recursion
    if (n==0):
        return 0
    else:
        return n + Suma(n-1)
#
def pascal(n):																	#Calcular triangulo de pascal por recursion
    if (n==1):
        return [1]
    else:
        Linea = [1]
        Previa_Linea = pascal(n-1)
        for i in range(len(Previa_Linea)-1):
            Linea.append(Previa_Linea[i] + Previa_Linea[i+1])
        Linea += [1]
    return Linea
#
print (fib(6))
print (Suma(6))
print (pascal(6))
input()
