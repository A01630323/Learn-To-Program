print ("**************")
print ("*** LISTAS ***")
print ("**************")

#Crear lista con algunos valores
print ("Crear lista con algunos valores")
list1=[1,"a",[True,"b",2],False]
print ("*********************************")

#Crear una lista vacia
print ("Crear una lista vacia")
list2=[]
print ("*********************************")

#Imprimir lista de forma lineal
print ("Imprimir lista de forma lineal")
list1=[1,"a",[True,"b",2],False]
list2=[]
print (list1)
print (list2)
print ("*********************************")

#Imprimir lista en forma vertical
print ("Imprimir lista en forma vertical")
list1=[1,"a",[True,"b",2],False]
for list1 in list1:
	print (list1)
print ("*********************************")

#Elemento de una lista
print ("Elemento de una lista")
list1=[1,"a",[True,"b",2],False]
print (list1[2])
print ("*********************************")

#¿Existe el elemento en la lista?
print ("¿Existe el elemento en la lista?")
list1=[1,"a",[True,"b",2],False]
print ("a" in list1)
print ("b" in list1)
print ("*********************************")

#Cantidad de elementos de la lista
print ("Cantidad de elementos de la lista")
list1=[1,"a",[True,"b",2],False]
list2=[]
print (len(list1))
print (len(list2))
print ("*********************************")

#Concatenar listas
list1=[1,2,3]
list2=[4,5,6]
print ("Concatenar listas")
list3=list1+list2
print (list3)
print ("*********************************")

#Repetir lista
print ("Repetir lista")
list1=[0]*4
print (list1)
list2=[7,8,9]*2
print (list2)
print ("*********************************")

#Imprimir rebanadas de lista
print ("Imprimir rebanadas de lista")
list1=['a','b','c','d','e','f','g']
print (list1[1:3])							#Imprime del elemento 1 al 3 sin mostrar el elemento 3
print (list1[:4])							#Imprime del elemento inicial hasta el 4 sin mostrar el elemento 4
print (list1[4:])							#Imprime desde el elemento 4 mostrandolo, hasta el final
print (list1[:])							#Imprime todos los elementos de la lista
print ("*********************************")

#Modificar listas
print ("Modificar listas")
list1=['a','b','c','d','e','f','g']
list1[2:4]=['x','y']						#Reemplazar los elementos del 2 al 4 sin reemplazar el elemento 4
print (list1)
list1=['a','b','c','d','e','f','g']
list1[2:4]=[]								#Eliminar los elementos del 2 al 4 sin eliminar el elemento 4
print (list1)
print ("*********************************")

#Añadir elemento al final de la lista
list1=[1,2,3,4,5]
list1.append(6)
print (list1)
print ("*********************************")

#Extender lista
print ("Extender lista")
list1=['a','b','c']
list2=['d','e']
list1.extend(list2)							#Extiende el valor de list1 sin modificar list2
print (list1)
print ("*********************************")

#Orden alfabetico
print ("Orden alfabetico")
list1=["Ruben","Barajas","Curiel","Escuela","Programacion"]
print (list1)
list1.sort()
print (list1)
print ("*********************************")

#Eliminar elementos de la lista
print ("Eliminar elementos de la lista metodo pop")
list1=['z','y','x','w','v','u']
Eliminado=list1.pop(1)						#Elimina el elemento 1 de la lista y lo guarda en un variable
print (list1)
print (Eliminado)
print ("Eliminar elementos de la lista metodo del")
list1=['z','y','x','w','v','u']
del list1[1]								#Elimina el elemento 1 de la lista
print (list1)
print ("Eliminar elementos de la lista metodo remove")
list1=['z','y','x','w','v','u']
list1.remove('y')							#Elimina el elemento "y" de la lista
print (list1)
print ("Eliminar elementos de la lista metodo del + rebanadas")
list1=['z','y','x','w','v','u']
del list1[1:3]								#Elimina los elementos desde 1 hasta 3, sin eliminar el elemento 3
print (list1)
print ("*********************************")
