print ("*********************************")
print ("*** TIEMPO RESPECTO A LA HORA ***")
print ("*********************************")
Hora = int(input("Que hora es (en formato 24 horas): "))
if(Hora<0 or Hora >23):
    print ("No escribiste la hora en formato de 24 horas")
if (Hora>=5 and Hora<12):
    print ("Es mañana")
if (Hora>=12 and Hora<20):
    print ("Es tarde")
if ((Hora>=0 and Hora <5)or(Hora>=20 and Hora <=23)):
    print ("Es noche")
input ()