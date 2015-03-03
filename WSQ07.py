print("********************************************")
print("*** SUMA DE NUMEROS EN UN RANGO DEFINIDO ***")
print("********************************************")
LimiteInferior=int(input("Rango inferior: "))
LimiteBajo=LimiteInferior
LimiteSuperior=int(input("Rango superior: "))
Total=0
while (LimiteInferior<=LimiteSuperior):
    Total=Total+LimiteInferior
    LimiteInferior=LimiteInferior+1
print ("La suma de los numeros entre",LimiteBajo,"y",LimiteSuperior," es: ",Total)
input ()
