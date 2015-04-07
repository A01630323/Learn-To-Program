print ("********************")
print ("*** DICCIONARIOS ***")
print ("********************")
#
Codigos={"Estufa":1234,"Lavadora":4567}						#Creacion de un diccionario
print (Codigos)
#
Codigos={"Estufa":1234,"Lavadora":4567}
Codigos["Licuadora"]=9876									#Añadir una clave
print (Codigos)
#
Codigos={"Estufa":1234,"Lavadora":4567}
Extraer= (Codigos["Lavadora"])								#Leer una clave
print(Extraer)
#
Codigos={"Estufa":1234,"Lavadora":4567}
del Codigos["Estufa"]										#Eliminar clave
print (Codigos)
#
Codigos={"Estufa":1234,"Lavadora":4567}
print (sorted(Codigos.keys()))								#Mostrar las claves solamente
#
Codigos={"Estufa":1234,"Lavadora":4567}
print ("Lavadora" in Codigos)								#Buscar clave en el diccionario
print ("Refrigerador" in Codigos)
#
input()
