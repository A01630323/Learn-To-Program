def Titulo():
	print("******************************************")
	print("*** CREAR, EDITAR Y LEER ARCHIVOS .txt ***")
	print("******************************************")
def Crear():
    Archivo=open('File.txt','w')
    Archivo.close()
#
def Escribir():
    Archivo=open('File.txt','a')
    Archivo.write('Ruben\n')
    Archivo.write('Barajas\n')
    Archivo.write('Curiel\n')
    Archivo.close()
#
def Leer():
    Archivo=open('File.txt','r')
    Lineas=Archivo.readlines()
    for a in Lineas:
        print (a)
    Archivo.close()
#
Titulo()
Crear()
Escribir()
Leer()
input()
