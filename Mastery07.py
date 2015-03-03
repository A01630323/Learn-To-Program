print ("**************************")
print ("*** USO DE COMENTARIOS ***")
print ("**************************")
                                                                                    # Espacio para hacer el programa claro.
Numero_Factorial = int(input("De que numero obtendremos el factorial: "))           # Amacenar en una variable INT el numero al que le sacaremos factorial
Contador=1                                                                          # Una variable contador inicializada.
Factorial=1                                                                         # Comenzar con el factorial de 0 o 1. Aqui se añadira el resultado.
while Contador<=Numero_Factorial:                                                   # Mientras que el contador no supere al numero que debemos obtener de factorial.
    Factorial=Factorial*Contador                                                    # Obtener el factorial de dicho numero.
    Contador=Contador+1                                                             # Incrementar el contador para acercarnos cada ves mas al factorial a obtener.
print ("El resultado es: ",Factorial)                                               # Una vez almacenado el resultado en una variable, mostrarlo en pantalla.                                                                                    # Espacio para hacer el programa claro.
input ()                                                                            # Una vez terminado el programa, deberemos presionar una tecla del teclado para salir de el.