import random                                                                       #Libreria de modulos aleatorios
print ("**************************************")
print ("*** ADIVINA UN NUMERO DEL 1 AL 100 ***")
print ("**************************************")
Verdadero=random.randint(1,100)                                                     #Guardar numero aleatorio
Contador=1
Numero=int (input("Cual numero seleccionas: "))
while (Verdadero != Numero):
    Contador=Contador+1                                                             #Contar cuantos intentos realizaste para adivinar
    if (Numero<Verdadero):
        Numero=int(input("Lo siento. El numero tiene un valor mas alto. Intenta denuevo: "))            #Pedir al usuario que adivine el numero
    else:
        Numero=int(input("Lo siento. El numero tiene un valor mas bajo. Intenta denuevo: "))            #Pedir al usuario que adivine el numero
       
print ("El numero correcto es: ",Verdadero)                                         #Ya adivino el numero. Mostrar cual era.
print ("Tu cantidad de intentos son: ",Contador)                                    #Mostrar cuantos intentos realizo
input ()
