def Titulo():										#Funcion que coloca un titulo al trabajo
	print ("****************************")
	print ("*** CALCULAR PALINDROMOS ***")
	print ("****************************")
#
def Invertir(C):									#Funcion que invierte el numero
	C=str(C)
	C=C[::-1]
	C=int(C)
	return C
#PROGRAMA PRINCIPAL
Titulo()
PalindromesNaturales=0
ConviertenPalindromes=0
LychrelCandidatos=0
Lychrel=[]
Datos=[]
X=int(input("Coloca el numero inferior: "))			#Introducir el rango de valores a analizar
Y=int(input("Coloca el numero superior: "))
print ("El rango de los numeros a analizar va de %s a %s" %(X,Y))
#
for i in range (Y-X+1):								#Transformar en lista, todos los numeros dentro del rango designado
	Datos.append(X)
	X=X+1
#
for a in Datos:										#Analizar cada numero del rango por separado
    Inverso1=Invertir(a)								#Primero, obtener su inverso
    if (a==Inverso1):
        PalindromesNaturales=PalindromesNaturales+1				#Si el numero inverso es igual al numero normal, se encontró un palindrome natural
    else:
        Suma=a+Inverso1										#Si el numero inverso no es igual al numero normal, ambos se deben sumar y dar un nuevo numero
        Inverso2=Invertir(Suma)							#Ademas, el nuevo numero debe volver a invertir para analizarlo nuevamente
        for b in range(30):									#Probar 30 veces, para saber si será candidato a numero Lychrel o se convertirá en palindrome
            if (Suma==Inverso2):
                ConviertenPalindromes=ConviertenPalindromes+1						#Si el numero y su inverso son iguales, significa que en algún momento de convirtió palindrome
                break												#Por lo tanto, salirse del ciclo y probar otro numero
            else:
                Suma=Suma+Inverso2									#Mientras tanto, intentar convertirlo en palindrome
                Inverso2=Invertir(Suma)
                if (b==29):											#Si ya pasaron 30 ciclos, el numero será candidato Lychrel
                    LychrelCandidatos=LychrelCandidatos+1
                    Lychrel.append(a)									#Añadir el numero a la lista de numeros Lychrel
print ("La cantidad de palindromes naturales son:",PalindromesNaturales)
print ("La cantidad de numeros que se convierten palindromes son:",ConviertenPalindromes)
print ("La cantidad de numeros Lychrel candidatos son:",LychrelCandidatos)
if (LychrelCandidatos!=0):							#¿Se encontraron candidatos de numero Lychrel?
	print ("Los numeros Lychrel candidatos son:")		#Si, entonces mostrarlos en pantalla
	print (Lychrel)
input ()
