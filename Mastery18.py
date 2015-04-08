print ("******************************")
print ("*** CONDICIONALES ANIDADOS ***")
print ("******************************")
print ("\f TIPO DE ESCUELA")
print ("\f 1.- Ingeniería")
print ("\f 2.- Licenciatura")
Carrera=int(input("A que tipo de escuela perteneces: "))
Calificacion=int(input("Cuanta calificacion sacaste (Escala del 0 al 10): "))
if (Carrera==1):
	if (Calificacion>=8):
		print ("Eres un todopoderoso")
	if (Calificacion>=7 and Calificacion<8):
		print ("Te comprendemos, estas en ingeniería")
	if (Calificacion<7):
		print ("Un error del profesor seguramente, jajaja")
if (Carrera==2):
	print ("Te dire algo: las licenciaturas son demaciado faciles")
if (Carrera!=1 and Carrera!=2):
	print ("No seleccionaste ninguna carrera")
input ()
