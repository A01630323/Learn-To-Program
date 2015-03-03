print ("**********************")
print ("*** CALIFICACIONES ***")
print ("**********************")
Cantidad=int(input("Cuantas calificaciones vas a ingresar: "))
Contador=1
Sumatoria=0
Promedio=0
while (Contador<=Cantidad):
    Calificacion=int(input("Inserta tu calificacion en formato del 0 al 100: "))
    Sumatoria=Sumatoria+Calificacion
    Contador=Contador+1
Promedio=Sumatoria/Cantidad
print ("Tu promedio es: ",Promedio)
input()