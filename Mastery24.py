print ("**************")
print ("*** TUPLES ***")
print ("**************")
Tuple=(1,'a',"Ruben",[2,'b'],True,(False,"Barajas"),3)		#Creacion de un tuple
print (Tuple)
Tuple[3][1]='z'												#Intentar modificar la lista dentro del tuple. SI SE PUEDE MODIFICAR
print (Tuple)
Tuple[4]=False												#Intentar modificar el tuple. NO SE PUEDE MODIFICAR
print (Tuple)
input ()
