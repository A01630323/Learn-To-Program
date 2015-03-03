def SUMA():
    print ("*** SUMA DE NUMEROS ***")
    print ("*** Funcion sin parametros ***")
    Numero1=float (input("Cual es el primer numero: "))
    Numero2=float (input("Cual es el segundo numero: "))
    TotalSuma=Numero1+Numero2
    print ("El total de la suma es: ",TotalSuma)
#
def RESTA(NumeroA,NumeroB):
    print ("*** RESTA DE NUMEROS ***")
    print ("*** Funcion con parametros de entrada ***")
    TotalResta=NumeroA-NumeroB
    print ("El total de la resta es: ",TotalResta)
#
def MULTIPLICACION(NumeroY,NumeroZ):
    print ("*** MULTIPLICACION DE NUMEROS ***")
    print ("*** Funcion con parametros de entrada y salida ***")
    TotalMultiplicacion=NumeroY*NumeroZ
    return TotalMultiplicacion
#
def DIVICION():
    print ("*** DIVICION DE NUMEROS ***")
    print ("*** Funcion sin parametros ***")
    NumeroR=float (input("Cual es el primer numero: "))
    NumeroS=float (input("Cual es el segundo numero: "))
    TotalDivicion=NumeroR/NumeroS
    print ("El total de la divicion es: ",TotalDivicion)
#
print ("************************")
print ("*** USO DE FUNCIONES ***")
print ("************************")
print ("MENU DE OPCIONES")
print ("    'S' o 's' = Sumar")
print ("    'R' o 'r' = Restar")
print ("    'M' o 'm' = Multiplicar")
print ("    'D' o 'd' = Dividir")
Operacion=input ("Selecciona la operacion que deceas realizar: ")
#
if (Operacion=='S' or Operacion=='s'):
    SUMA()
#
if (Operacion=='R' or Operacion=='r'):
    NumeroA=float (input("Cual es el primer numero: "))
    NumeroB=float (input("Cual es el segundo numero: "))
    RESTA(NumeroA,NumeroB)
#
if (Operacion=='M' or Operacion=='m'):
    NumeroY=float (input("Cual es el primer numero: "))
    NumeroZ=float (input("Cual es el segundo numero: "))
    TotalMultiplicacion=MULTIPLICACION(NumeroY,NumeroZ)
    print ("El total de la multiplicacion es: ",TotalMultiplicacion)
#
if (Operacion=='D' or Operacion=='d'):
    DIVICION()
#
input ()