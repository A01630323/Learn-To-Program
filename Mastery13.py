import random
import winsound
#
def Titulo():
	print ("************************")
	print ("*** IMPORTAR MODULOS ***")
	print ("************************")
#
print (random.randint(1,10))									#Mostrar numero aleatorio del 1 al 10
print (random.randrange(20,30,2))								#Mostrar numero aleatorio del 20 al 30. Solo numeros pares
#
winsound.Beep(1000, 2000)										#Sonido a 1KHz durante 2s
winsound.PlaySound("*", winsound.SND_ALIAS)						#Sonido de bloqueado de Windows
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)			#Sonido de apagar sistema de Windows
input ()
