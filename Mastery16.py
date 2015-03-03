print ("********************")
print ("*** AÑO BISIESTO ***")
print ("********************")
Tiempo = int(input("Coloca el año que deceas saber: "))
Prueba = Tiempo%4
if (Prueba==0):
    print ("El año",Tiempo,"es bisiesto")
else:
    print ("El año",Tiempo,"no es bisiesto")
input ()